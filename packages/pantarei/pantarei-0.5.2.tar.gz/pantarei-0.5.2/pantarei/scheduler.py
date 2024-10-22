"""
Scheduler
"""
from .helpers import serialize_kwargs, rmd, mkdir
from .backends import detect
import inspect
import subprocess
import dill

# TODO: add default scheduler, to avoid that each job constructs a new one
# Encapsulate what varies:

# Public:
# submit()
# wait()
# queued()

class Scheduler:

    """
    Wrapper to scheduler for execution on a distributed memory environment

    `Scheduler` is entirely decoupled from `Job`. For job submission,
    it only needs a script as a string and the relevant job
    directives.
    """

    # TODO: add custom header or args to __init__ so that we can customize the job at run time

    def __init__(self, host='localhost', verbose=False, backend='auto', jobs_limit=0):
        """
        :param host: hostname of the cluster
        :param verbose: verbose output
        :param backend: backend for scheduler (default is auto-detect)
        :param jobs_limit: maximum number of jobs to run concurrently (if 0 no limit)
        """
        self.host = host
        self.verbose = verbose
        self.path = ''  # working directory?
        self.backend = detect(backend)
        self.jobs_limit = jobs_limit

    def wait(self, job_name=None, max_jobs=None, seconds=5):
        """
        Wait until `job_name` is done or until there are less than `max_jobs`

        The check is done every `seconds` seconds.
        """
        import os
        import subprocess
        import time

        assert not (job_name and max_jobs), 'set only one of these parameters'
        muted = False
        while True:
            if job_name is None:
                must_wait = len(self.queue()) > 0
            else:
                # Make sure job_name is a list
                if isinstance(job_name, str):
                    job_name = [job_name]
                must_wait = any([self.queued(name) for name in job_name])

            if max_jobs is not None:
                # print('must', len(self.queue()), len(self.queue()) > max_jobs)
                must_wait = len(self.queue()) >= max_jobs

            if must_wait:
                if self.verbose and not muted:
                    print('waiting...')
                    muted = True
                from . import core
                if core.mode == 'timid':
                    import sys
                    print('...cannot proceed further in timid mode\n')
                    sys.exit()
                else:
                    time.sleep(seconds)
            else:
                break

    def queue(self):
        """Return a list of jobs in the scheduler queue"""
        output = subprocess.check_output(self.backend['queue'], shell=True)
        queued_jobs = output.decode().split('\n')[:-1]
        return queued_jobs

    # TODO: this seems redundant, job checks against the fqn so we should test if fqn in queue()
    def queued(self, job_name):
        """Return `True` the job named `job_name` is queued.

        :param job_name: fqn or a regexp matching a fully qualified name
        """
        import re
        # Check if job_name is fully qualified
        # if re.match('.*-.*', job):
        for queued_job in self.queue():
            # We clear the match afterwards because it cannot be pickled by dill
            match = re.match(job_name, queued_job)
            if match:
                del match
                return True
        return False

    def submit(self, script, job_name, job_output=None, job_error=None, cores=1):
        """
        Submit a script for batch execution on the scheduler

        :param script: string of python commands to execute
        :param job_name: name of job
        :param job_output: job output file
        :param job_error: job error file
        :param cores: number of cores for the job
        """
        name, output, error = job_name, job_output, job_error
        params = locals()
        # command = 'python -u -'
        # header = ''

        # TODO: not the best place probably
        if self.backend['limit'] and self.jobs_limit == 0:
            ncores = subprocess.check_output(['grep', '-c', '^processor', '/proc/cpuinfo'])
            self.wait(max_jobs=int(ncores))

        if self.jobs_limit > 0:
            self.wait(max_jobs=self.jobs_limit)

        # Assemble script spefications according to backend
        directive = self.backend["directive"]
        args = []
        for name, flag in self.backend['specifications'].items():
            if name not in params:
                continue
            value = params[name]
            if value is not None:
                args.append(f'{directive} {flag} {value}')

        # TODO: strip spaces when preceeded by = (like '-l nodes= 1' should be '-l nodes=1')

        # Define prologue and epilogue
        prologue = ''
        epilogue = ''
        
        # The backend uses batch jobs
        header = '\n'.join(args)
        # Interpolate script with job header
        if script.startswith('#!'):
            lines = script.split('\n')
            shebang = lines.pop(0)
            body = '\n'.join(lines)
        else:
            body = script
            shebang = '#!/usr/bin/env python'
            
        # Submit the job
        # TODO: are the env vars propagated here?
        output = subprocess.check_output(f"""{self.backend['submit']} <<'EOF'
{shebang}
{header}
{prologue}
{body}
{epilogue}
EOF""", shell=True)
        if self.verbose:
            print(output)
