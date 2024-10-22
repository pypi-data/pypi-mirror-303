#!/usr/bin/env python

import os
from pantarei.parsers import parse_yaml, parse_pickle
from pantarei.core import logos

    
def _state(path):        
    job_file = os.path.join(path, 'job.yaml')
    task_file = os.path.join(path, 'task.yaml')
    state = ''
    if not os.path.exists(job_file):
        if os.path.exists(task_file):
            db = parse_yaml(task_file)
            if 'task_end' in db:
                state = 'ended'                
            elif 'task_start' in db:
                state = 'running'                
            elif len(db) == 0:
                state = 'unknown'
    else:
        db = parse_yaml(job_file)
        if 'job_fail' in db:
            state = 'failed'                
        elif 'job_end' in db:
            state = 'ended'                
        elif 'job_start' in db:
            state = 'running'                
        elif 'job_queue' in db:
            state = 'queued'                
        elif len(db) == 0:
            state = 'unknown'
        else:
            raise ValueError(f'wrong state {list(db.keys())} in {path}')            
    return state

def _kind(path):
    job_file = os.path.join(path, 'job.yaml')
    task_file = os.path.join(path, 'task.yaml')
    if os.path.exists(job_file):
        return 'job'
    if os.path.exists(task_file):
        return 'task'
    return 'unknown'    

def _duration(path):
    """Current duration of job. If job is ended, return the elapsed duration"""
    import time
    import datetime
    
    job_file = os.path.join(path, 'task.yaml')
    if not os.path.exists(job_file):
        return datetime.timedelta(seconds=0)
    else:
        db = parse_yaml(job_file)
        if 'task_start' in db and 'task_end' in db:
            delta = float(db['task_end']) - float(db['task_start'])
        elif 'task_start' in db:
            delta = time.time() - float(db['task_start'])
        else:
            delta = 0
        return datetime.timedelta(seconds=int(delta))

def _split_names(path):
    import os
    root, base = os.path.split(path.rstrip('/'))
    root, func_tag = os.path.split(root.rstrip('/'))
    qn = func_tag + '/' + base
    func_tag = func_tag.split('-')
    if len(func_tag) == 1:
        func, tag = func_tag[0], ''
    else:
        func = func_tag[0]
        tag = '-'.join(func_tag[1:])
    return func, tag, qn

def _arguments(path):
    job_file = os.path.join(path, 'arguments.pkl')
    if os.path.exists(job_file):
        return parse_pickle(job_file)
    return {}

def _artifacts(path):
    if os.path.exists(os.path.join(path, 'arguments.pkl')):
        args = parse_pickle(os.path.join(path, 'arguments.pkl'))
        if "artifacts" in args:
            return args["artifacts"].format(**args)        
    if os.path.exists(os.path.join(path, 'results.pkl')):
        results = parse_pickle(os.path.join(path, 'results.pkl'))
        if isinstance(results, dict) and 'artifacts' in results:
            return results['artifacts']

        
class _Job:

    def __init__(self, path):
        import os
        self.path = path
        self._setup(path)

    def _setup(self, path):
        self.state = _state(path)
        self.duration = _duration(path)
        self.name, self.tag, self.qualified_name = _split_names(path)
        self.artifacts = _artifacts(path)
        self.logo = logos[self.state]
        self.kind = _kind(path)

        if self.state == '':
            self.kwargs = []
            self.pretty_name = f'{self.name}(...?...)'
        else:
            self.kwargs = _arguments(path)
            args = []
            for key in self.kwargs:
                # if self.task.ignore is not None:
                #     if key in self.task.ignore:
                #         continue
                if isinstance(self.kwargs[key], str):
                    args.append(f'{key}="{self.kwargs[key]}"')
                else:
                    args.append(f'{key}={self.kwargs[key]}')        
            kwargs = ','.join(args)
            self.pretty_name = f'{self.name}({kwargs})'
        
        # if os.path.join(os.path.dirname(path), 'metadata.pkl'):
        #     func_md = parse_pickle(os.path.join(os.path.dirname(path), 'metadata.pkl'))
        # self.docstring = func_md['docstring']
        # self.signature_args = func_md['args']
        # self.signature_kwargs = func_md['kwargs']

def load_from_path(path):
    import os
    from pantarei.parsers import parse_yaml, parse_pickle
    if os.path.join(path, 'task.yaml'):
        task_md = parse_yaml(os.path.join(path, 'task.yaml'))
    if os.path.join(path, 'job.yaml'):
        job_md = parse_yaml(os.path.join(path, 'job.yaml'))
    if os.path.join(path, 'arguments.pkl'):
        args = parse_pickle(os.path.join(path, 'arguments.pkl'))
    if os.path.join(path, 'results.pkl'):
        results = parse_pickle(os.path.join(path, 'results.pkl'))
    if os.path.join(os.path.dirname(path), 'metadata.pkl'):
        func_md = parse_pickle(os.path.join(os.path.dirname(path), 'metadata.pkl'))
    # print(task_md)
    # print(job_md)
    # print(args)
    # print(results)

    root, base = os.path.split(path.rstrip('/'))
    root, func_tag = os.path.split(root.rstrip('/'))
    qn = func_tag + '/' + base
    func_tag = func_tag.split('-')
    if len(func_tag) == 1:
        func, tag = func_tag[0], ''
    else:
        func, tag = func_tag
    from pantarei.task import Task
    task = Task(None, name=func, tag=tag,
                qualified_name=qn,
                docstring=func_md['docstring'],
                signature_args=func_md['args'],
                signature_kwargs=func_md['kwargs'])
    # TODO: arghhhh, the qualified name takes only the non-default arguments
    # but in arguments.yaml we give all the arguments.
    # So atm we cannot reconstruct the task from the dataset... :-(
    
    # 1. if we stored the function, we could strip the default arguments (difficult)
    # 2. also store the explicit kwargs in a separate yaml (but careful to hide it)
    # 3. do not store the default arguments
    # 4. allow the fqn as argment in the constructor and use it in the property in case

    # We should stick to the non default args. The reason is:
    # if we add an optional argument to a function, we do not want the fqn to change!
    # We want it to be backward compatible.
    # TODO: for the artifacts we need the function... because of these
    # all_kwargs = all_actual_kwargs(self.func, *args, **kwargs)
    # kwargs = actual_kwargs(self.func, *args, **kwargs)        
    # name = self.qualified_name(**kwargs)
    # I think we cannot keep Task, we need a custom artifacts accessor
    # The reason is that in Task we always look up the passed arguments
    # but doing this requires to inspect the function signature.
    # Could we bypass the above wrapping if we only pass kwargs?
    # Note we must pass all kwargs...
    # We could simply dill the function... so point 1. above.
    # Actually, it would be useful to at least have the docstring
    # we could store globally the default arguments
    # Then in the task constructor we should store the signature and / or the default arguments
    # In the other calls we would not need to store anything

    # args = {key: value for key, value in args.items()}
    
    print(task.name(), ':', task.doc, args, 'artifacts:', task.artifacts(**args))
        
def run(script, *, timid=False, clean=False, scratch=False, veryclean=False, args=''):
    import subprocess
    mode = ''
    if timid:
        mode = 'pantarei=timid'
    if clean:
        mode = 'pantarei=clean'
    if veryclean:
        mode = 'pantarei=veryclean'
    if scratch:
        mode = 'pantarei=scratch'

    # TODO: careful here, this way of calling will propagate the env vars down to the very script which is submitted
    # So either we clear them there, or they will interfere with the path report
    # It should not matter for the job because we execute the task, but still it is not good
    output = subprocess.check_output(f'{mode} pantarei_report=1 python {script} {args}',
                                     shell=True)
    print(output.decode().strip())

def _lines(script, verbose=False):
    import subprocess
    mode = 'pantarei=timid pantarei_report=1'
    output = subprocess.check_output(f'{mode} python {script}', shell=True)
    output = output.decode().strip().split('\n')
    if verbose:
        print('\n'.join(output))
    try:
        line = output.index('# pantarei paths:')
        lines = output[line+1:]
        return lines
    except ValueError:
        return []

def _public_args(x):
    return {key: value for key, value in x.__dict__.items() if not key.startswith('_')}

def report(script, *, fmt='path', args=''):
    # print('\n'.join(output[line+1:]))
    lines = _lines(script + ' ' + args)
    fmt = [_.strip() for _ in fmt.split(',')]
    fmt = ' '.join(['{' + _ + '}' for _ in fmt])
    for path in lines:
        job = _Job(path)
        kwargs = _public_args(job)
        # TODO: artfiacts should expand (on multiple lines?) if a list
        print(fmt.format(**kwargs))

def summary(script, *, args='', only=('failed', )):
    lines = _lines(script + ' ' + args)
    jobs = []
    for path in lines:
        job = _Job(path)
        jobs.append(job)
    from pantarei.core import _report
    print('\n'.join(_report(jobs, only=only)))

def artifacts(script, *, args=''):
    for path in _lines(script + ' ' + args):
        job = _Job(path)
        if job.artifacts is not None:
            print(job.artifacts)

def _inspect(path):
    job_file = os.path.join(path, 'job.out')
    if os.path.exists(job_file):
        print('-', job_file)
        with open(job_file) as fh:
            content = fh.read()
            print(content.strip())
        print()

def inspect(*paths):
    for path in _paths(paths):
        _inspect(path)

def _run(cmd):
    import subprocess
    results = subprocess.run(cmd, shell=True, capture_output=True)
    if results.returncode != 0:
        print(results.stderr.decode())
        raise RuntimeError(f'command failed: {cmd}')
        
def _copy(path, dest, strip_tmp=False):

    if not os.path.exists(path):
        print(f'skipping non-existed job path: {path}')
        return
    
    _run(f'rsync -uvaR ././{path} {dest}')
    
    job = _Job(path)
    if job.artifacts is not None:
        source = job.artifacts        
        if strip_tmp and source.startswith('/tmp/'):
            source = source[5:]

        if os.path.exists(source):
            if job.artifacts.startswith('/'):
                _run(f'rsync -uvaR {source} {dest}')
            else:
                _run(f'rsync -uvaR ././{source} {dest}')
        else:
            print(f'skipping non-existed job artifacts: {source}')
            return

def _paths(paths):
    # if len(paths) == 0:
    if len(paths) == 1 and paths[0] == '-':
        import sys
        paths = [path.rstrip() for path in sys.stdin]            
    return paths
        
        
def copy(*paths, dest=None, strip_tmp=False, args=''):
    assert dest is not None

    # If we pass a script, we grab the job paths
    # and then proceed
    if len(paths) == 1 and os.path.isfile(paths[0]):
        paths = _lines(paths[0] + ' ' + args)

    # We now have a list of job paths
    for path in _paths(paths):
        _copy(path, dest, strip_tmp=strip_tmp)

def main():
    import argh
    argh.dispatch_commands([run, report, summary, artifacts, inspect, copy])
        
if __name__ == '__main__':
    main()
