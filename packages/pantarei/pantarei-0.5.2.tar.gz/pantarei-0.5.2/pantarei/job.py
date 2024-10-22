"""
Job
"""
import os
import time
import inspect
import dill
import subprocess

from . import core
from .scheduler import Scheduler
from .helpers import mkdir, serialize_kwargs, rmd

class JobFailure(Exception):
    """Exception raised when a failed job is found in the session"""
    pass

def _load_yaml(path):
    with open(path) as fh:
        db = {}
        for line in fh:
            key, value = line.split(':')
            db[key] = value
    return db


_stack_index = -1

class Job:

    """
    Batch execution on distibuted memory environment (ex. scheduler)
    """

    mode = core.mode

    def __init__(self, task, scheduler=None, cores=1, wall_time=None,
                 output=None, error=None,
                 **kwargs):
        """
        :param task: the `Task` to execute
        :param scheduler: the scheduler to usel if `None` it will be auto-detected
        :param cores: number of cores to use
        :param wall_time: the maximum wall time
        :param output: output file
        :param error: error file
        """
        self.task = task
        self.scheduler = scheduler
        self.cores = cores
        self.wall_time = wall_time
        self.output = output
        self.error = error
        # Arguments for task (as keyword arguments only)
        self.kwargs = kwargs

        # This will autodetect a scheduler on localhost
        if self.scheduler is None:
            self.scheduler = Scheduler(backend='auto')

    @property
    def path(self):
        """Path to the cache of the job"""
        return os.path.join(self.task.cache.path, self.qualified_name())

    def name(self):
        """General name of job (independent of arguments)"""
        return self.task.name(**self.kwargs)

    def qualified_name(self):
        """Unique name of job"""
        return self.task.qualified_name(**self.kwargs)

    def pretty_name(self):
        """Pretty printed name of job (with args)"""
        args = []
        for key in self.kwargs:
            if self.task.ignore is not None:
                if key in self.task.ignore:
                    continue
            if isinstance(self.kwargs[key], str):
                args.append(f'{key}="{self.kwargs[key]}"')
            else:
                args.append(f'{key}={self.kwargs[key]}')
        kwargs = ','.join(args)
        return f'{self.task.name()}({kwargs})'

    def clear(self, **kwargs):
        """Clear undelrying task and its artifacts"""
        self.task.clear(self.task, **kwargs)
        # Clear job artifacts too
        rmd(self.path)
        
    # TODO: drop?
    def done(self, **kwargs):
        """Return True is Job is done"""
        # TODO: add condition on job execution
        if hasattr(self.task, 'done'):
            return self.task.done(**kwargs)
        return False

    @property
    def artifacts(self):
        """Job artifacts, possibly as a sequence"""
        return self.task.artifacts(**self.kwargs)
            
    @property
    def duration(self):
        """Current duration of job. If job is ended, return the elapsed duration"""
        import datetime
        job_file = os.path.join(self.path, 'job.yaml')
        if not os.path.exists(job_file):
            return datetime.timedelta(seconds=0)
        else:
            db = _load_yaml(job_file)
            if 'job_start' in db and 'job_end' in db:
                delta = float(db['job_end']) - float(db['job_start'])
            elif 'job_start' in db:
                delta = time.time() - float(db['job_start'])
            else:
                delta = 0
            return datetime.timedelta(seconds=int(delta))

    @property
    def state(self):
        """
        State of job. 

        Possible values:
        - failed
        - ended
        - running
        - queued
        - unknown       
        """
        job_file = os.path.join(self.path, 'job.yaml')
        if not os.path.exists(job_file):
            return ''
        else:
            db = _load_yaml(job_file)
            if 'job_fail' in db:
                return 'failed'
            elif 'job_end' in db:
                return 'ended'
            elif 'job_start' in db:
                # return 'started'
                return 'running'
            elif 'job_queue' in db:
                return 'queued'
            elif len(db) == 0:
                return 'unknown'
            else:
                raise ValueError(f'wrong state {list(db.keys())} in {self.path}')

    def __call__(self, **kwargs):
        # If no arguments are passed than we assume they were passed
        # to the constructor
        if len(kwargs) > 0:
            self.kwargs = kwargs

        # Add this to global list, make a snapshot for transient jobs
        from copy import deepcopy
        # TODO: we can drop the idea of making snapshots of jobs, just store the qns
        # This should make the code a bit faster too...
        from pantarei import core
        core._jobs.append(deepcopy(self))
        core.jobs.append(self.qualified_name())

        # This is not properly done atm, but it should work.
        # 
        # The point is that without the line below, when the task is not done, the wrapped job
        # will not store its path anywhere, and will be missing. Jobs that are not ended would be phantom
        # TODO: improve this
        from . import core
        core._tasks.append(self.task.cache._storage(self.qualified_name()))

        assert self.mode in ['safe', 'brave', 'timid', 'clean', 'veryclean', 'scratch']
        if self.mode == 'timid':
            if self.task.done(**self.kwargs):
                return self.task(**self.kwargs)
        elif self.mode == 'scratch':
            self.clear(**self.kwargs)
            self._submit()
        elif self.state == 'failed' and self.mode == 'safe':
            raise JobFailure(f'stop because of previous job failure {self.qualified_name()}')
        elif self.state == 'failed' and self.mode == 'brave':
            # TODO: this should only be done if there are no deps
            print(f'WARNING: skipping failed job {self.qualified_name()}')
        elif self.state == 'failed' and self.mode == 'clean':
            self.clear(**self.kwargs)
        elif self.mode == 'veryclean':
            self.clear(**self.kwargs)
        elif self.task.done(**self.kwargs):
            return self.task(**self.kwargs)
        elif self.state in ['running', 'queued']:
            # Job is running (ex. on a remote cluster), we skip right away
            pass
        elif self.scheduler.queued(self.qualified_name()):
            # Do nothing if job is in queue
            pass
        else:
            self._submit()

        # We reset the arguments if they were passed to __call__
        if len(kwargs) > 0:
            self.kwargs = {}

    def _submit(self):        
        # dirname = os.path.join(self.task.cache.path, self.qualified_name())
        mkdir(self.path)
        session_pkl = os.path.join(self.path, '.session.pkl')
        context_pkl = os.path.join(self.path, '.context.pkl')
        job_state = os.path.join(self.path, 'job.yaml')
        job_output = os.path.join(self.path, 'job.out')
        kwargs = serialize_kwargs(self.kwargs)

        n = _stack_index
        n = -2  # for
        # s = stacks[n]
        stacks = inspect.stack()
        s = stacks[n]
        for n in range(len(stacks)-1, -1, -1):
            if 'job' in stacks[n].frame.f_locals:
                s = stacks[n]
                # print('FOUND', n)
                # from .helpers import debug_stacks
                # debug_stacks([s])
                break            

        # fix issues with emacs python shell execution
        # TODO: this should not be needed anymore
        var = s.frame.f_locals
        if '__pyfile' in var:
            # s = stacks[-2]
            s = stacks[n - 1]
            garbage = var.pop('__pyfile')
            del garbage

        # Attempt to clear the imported module session for pickling
        # var = s.frame.f_locals
        # if '__builtins__' in var:
        #     for clear in ['__builtins__', '__cached__']:
        #         garbage = var.pop(clear)
        #         del garbage
        #         var['__cached__'] = None
        #         var['__name__'] = '__main__'
        #         var['__package__'] = None
        #         var['__spec__'] = None
                
        #import pprint
        #pprint.pprint(s.frame.f_locals)
        #pprint.pprint(s.frame.f_globals)
            
        from types import ModuleType
        context = ModuleType('context')
        # context.__dict__.update(s.frame.f_globals)
        # args = s.frame.f_locals
        # import pprint
        # pprint.pprint(s.frame.f_locals)
        # pprint.pprint(s.frame.f_globals)
        # context.__dict__.update(s.frame.f_globals)
        context.job = s.frame.f_locals['job']
        # Store session and local context separately.
        # The session stores all objects in the module of the frame
        # containing the job instance
        dill.dump_module(session_pkl, module=inspect.getmodule(s.frame.f_code), refimported=True)
        # The context session stores the job instance itself
        # to cover the case in which this is defined in a function
        # TODO: query cannot be pickled in context? How come, we only have job here...
        # print('query' in s.frame.f_globals)
        # print('query' in s.frame.f_locals)
        # Nothing of this works
        # query = s.frame.f_globals.pop('query')
        # del query
        # s.frame.f_locals.pop('query')
        dill.dump_module(context_pkl, module=context, refimported=True)
        # print(context_pkl)
        # print(session_pkl)
        # from .helpers import debug_stacks
        # debug_stacks(stacks)

        # print('---------------')
        # print(s.frame)
        # print(s.frame.f_locals)
        # print('---------------')

        # TODO: at the line of the called there should be a Job instance
        # else it
        # for s in stacks[:0:-1]:
        #     print(s.frame, s.frame.f_lineno, s.frame.f_code.co_name)
        #     #print(s.frame.f_code)
        #     j = s.frame.f_lineno - s.frame.f_code.co_firstlineno
        #     src, _ = inspect.getsourcelines(s.frame.f_code)
        #     found = False
        #     for i, l in enumerate(src):
        #         if i == j:
        #             if l.strip().startswith('job('):
        #                 print(i, l.strip())
        #                 found = True
        #             break
        #     if found:
        #         break
        # print(s.frame.f_locals)
        # https://stackoverflow.com/questions/1253528/is-there-an-easy-way-to-pickle-a-python-function-or-otherwise-serialize-its-cod
        # TODO: process the calling line to get the job object instead of hardcoding job
        script = f"""\
#!/usr/bin/env -S python -u
__name__ = '__main__'
import sys
import os
import time
import dill
sys.path.append('.')

while True:
    if os.path.exists('{job_state}'): break

hostname = 'unknown'
if 'HOSTNAME' in os.environ:
    hostname = os.environ['HOSTNAME']

# We must unset the env variables else we get a report at the end
if 'pantarei' in os.environ:
    del os.environ['pantarei']
if 'pantarei_report' in os.environ:
    del os.environ['pantarei_report']
# print('mode', 'pantarei' in os.environ)
# print('report', 'pantarei_report' in os.environ)

fh = open('{job_state}', 'a')
print('job_node:', hostname, file=fh, flush=True)
print('job_start:', time.time(), file=fh, flush=True)
try:
    dill.load_module('{session_pkl}')
    context = dill.load_module('{context_pkl}')
    #import pprint
    #pprint.pprint(locals())
    #pprint.pprint(globals())
    #print()
    #pprint.pprint(context.__dict__)
    context.job.task({kwargs})
    #job.task({kwargs})
except:
    print('job_fail:', time.time(), file=fh, flush=True)
    raise
else:
    print('job_end:', time.time(), file=fh, flush=True)
finally:
    fh.close()
    # Remove session data when job is over
    os.remove('{session_pkl}')
    os.remove('{context_pkl}')
"""
        # TODO: drop this, it was only for synchronous, scheduler should always be not None
        if self.scheduler is None:
            import time
            with open(f'{job_state}', 'w') as fh:
                print('job_queue:', time.time(), file=fh, flush=True)

        self.scheduler.submit(script, self.qualified_name(), job_output=job_output,
                              job_error=None)

        # Job is queued
        if self.scheduler is not None:
            import time
            with open(f'{job_state}', 'w') as fh:
                print('job_queue:', time.time(), file=fh, flush=True)
