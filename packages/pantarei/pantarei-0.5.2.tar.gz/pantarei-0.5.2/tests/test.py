import unittest
import os

from pantarei import *

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_itemize(self):
        import numpy
        from pantarei.cache import _itemize
        a = numpy.array([numpy.array(1.0)])
        #print(type(a[0]), type(_itemize(a)[0]))
        self.assertTrue(isinstance(_itemize(a), list))
        self.assertTrue(isinstance(_itemize(a)[0], float))        
        b = {'a': a}
        self.assertTrue(isinstance(_itemize(b)['a'], list))
        self.assertTrue(isinstance(_itemize(b)['a'][0], float))
        a = numpy.array([numpy.array(1)])
        self.assertTrue(isinstance(_itemize(a)[0], int))
        b = {'a': a}
        self.assertTrue(isinstance(_itemize(b)['a'][0], int))
        import yaml

        a = numpy.array([1.0])[0]
        self.assertTrue(isinstance(_itemize(a), float))        
        #print(type(a))
        #print(yaml.dump(_itemize({'a': a})))
        
    def test_task_cache(self):
        import time
        def f(x):
            time.sleep(1)
            return x
        cache = Cache('/tmp/data')
        task = Task(f, cache=cache)
        data = task(x=1)
        self.assertEqual(data, 1)
        self.assertTrue(task.done(x=1))
        ti = time.time()
        task(x=1)
        tf = time.time()
        self.assertLess(tf-ti, 0.9)
        task.clear(x=1)
        self.assertFalse(task.done(x=1))
        ti = time.time()
        task(x=1)
        tf = time.time()
        self.assertGreater(tf-ti, 0.9)

        # Check with arrays
        # We should have a look at the .*.yaml files
        import numpy
        data = task(x=numpy.ndarray([1]))
        data = task(x=numpy.ndarray([1]))
        
    def test_task_ignore(self):
        import time
        def f(x, debug):
            return x
        cache = Cache('/tmp/data')
        task = Task(f, cache=cache, ignore=['debug'])
        task(x=1, debug=False)
        self.assertTrue(task.done(x=1, debug=True))
        self.assertTrue(task.done(x=1, debug=False))

    def test_task_default_args(self):
        import time
        def f(x):
            return x
        cache = Cache('/tmp/data')
        task = Task(f, cache=cache)
        qn1 = task.qualified_name(x=1)
        # Now add an optional argument
        def f(x, y=0):
            return x
        # The qualified name must be the same
        qn2 = task.qualified_name(x=1)
        self.assertEqual(qn1, qn2)

    def test_precision(self):
        """
        If relative difference between input floats is less than 1e-12
        then two tasks have the same qualified name (same hash). Also
        check that 0-sized arrays and floats are indistinguishable.
        """
        import time
        import numpy
        def f(x):
            return x
        cache = Cache('/tmp/data')
        task = Task(f, cache=cache)
        qn1 = task.qualified_name(x=numpy.pi)
        qn2 = task.qualified_name(x=numpy.pi + 1e-14)
        self.assertEqual(qn1, qn2)
        qn3 = task.qualified_name(x=numpy.pi + 1e-10)
        self.assertNotEqual(qn1, qn3)
        qn1 = task.qualified_name(x=numpy.array(numpy.pi))
        qn2 = task.qualified_name(x=numpy.pi)
        self.assertEqual(qn1, qn2)
        
    def test_task_clear_first(self):
        import time
        def f(x):
            return x
        cache = Cache('/tmp/data')
        task = Task(f, cache=cache, clear_first=True)
        task(x=2)

        # We now change the function output.
        # The cache will be used, unless we force execution
        # by first clearing the cache
        def f(x):
            return x**2
        task = Task(f, cache=cache, clear_first=True)
        self.assertFalse(task.done(x=2))
        self.assertEqual(task(x=2), 4)

    def test_task_artifacts_results(self):
        import time
        from pantarei.helpers import mkdir
        def f(x):
            output = '/tmp/artifacts_bis'
            mkdir(output)
            return {'y': x, 'artifacts': output}
        cache = Cache('/tmp/data')
        task = Task(f, cache=cache)
        task(x=1)
        self.assertTrue(os.path.exists('/tmp/artifacts_bis'))
        self.assertTrue(os.path.exists(cache._storage(task.qualified_name(x=1))))
        task.clear(x=1)
        self.assertFalse(os.path.exists('/tmp/artifacts_bis'))
        self.assertFalse(os.path.exists(cache._storage(task.qualified_name(x=1))))

    def test_task_artifacts(self):
        import time
        from pantarei.helpers import mkdir
        def f(x, output='/tmp/artifacts', artifacts='/tmp/artifacts'):
            mkdir(output)
            return x
        cache = Cache('/tmp/data')
        task = Task(f, cache=cache)
        task(x=1)
        self.assertTrue(os.path.exists(cache._storage(task.qualified_name(x=1))))
        self.assertTrue(os.path.exists('/tmp/artifacts'))
        task.clear(x=1)
        self.assertFalse(os.path.exists('/tmp/artifacts'))
        self.assertFalse(os.path.exists(cache._storage(task.qualified_name(x=1))))

    #@unittest.skip('Job not working from unittest')
    def test_job(self):
        import pantarei.job
        from pantarei import Task, Job, Scheduler, Cache
        #pantarei.job._stack_index = 2 #-1
        def f(x):
            import time
            time.sleep(1)
            return x
        task = Task(f, cache=Cache('/tmp/data'))
        job = Job(task, scheduler=Scheduler(backend='nohupx', verbose=False))
        job(x=1)
        job.scheduler.wait(seconds=1.5)
        from pantarei.core import orphans, _report, _jobs
        missing = orphans()
        #self.assertTrue(len(missing) == 0)
        _report(_jobs)
        

    def test_job_cmd(self):
        self.skipTest('broken on CI')
        script = """
from pantarei import Task, Job, Scheduler, Cache

def f(x):
    import time
    time.sleep(1)
    return x
task = Task(f, cache=Cache('/tmp/data'))
job = Job(task, scheduler=Scheduler(backend='nohupx', verbose=False))
job(x=1)
job.scheduler.wait(seconds=1.5)

from pantarei.core import orphans, _report, _jobs
missing = orphans()
_report(_jobs)
"""
        with open('test_pantarei.py', 'w') as fh:
            fh.write(script)
        import subprocess
        output = subprocess.check_output(['python', 'test_pantarei.py'])
        # print(output.decode())
        from pantarei.helpers import rmf
        rmf('test_pantarei.py')

    def test_job_clear_artifacts(self):
        self.skipTest('broken on CI')
        import os
        
        def f(x, y, artifacts='/tmp/data/y{y}.txt'):
            import os
            from pantarei.helpers import mkdir
            mkdir(os.path.dirname(artifacts))
            with open(artifacts.format(**locals()), 'w') as fh:
                fh.write(f'x={x}')
            return x

        cache = Cache('/tmp/data')
        job = Job(Task(f, cache=cache))
        job(x=1, y=0)
        assert job.task.artifacts(x=1, y=0) is not None
        # Note: In the stored _jobs there is no references to the full passed args and kwargs
        # so we cannot reconstruct the artifacts. We should store a copy of it as _artifacts
        # If it is not None it is returned.
        # The strategy is to reconstruct a dumb Job from the database, without actual function,
        # to just inspect the artifacts. We need the name of the function to be stored somewhere?
        # Or have a TaskReadOnly or TaskCopy something, which implements the relevant part of the interface
        # or perhaps stateful version, that is, its parameters are fixed.
        # Or perhaps a TaskView, which is linked to a path of the database.
        from pantarei.core import _jobs
        print(job.task.artifacts(x=1, y=0))
        import subprocess
        print('')
        subprocess.run('ls -l /tmp/', shell=True)
        print('')
        self.assertTrue(os.path.exists(job.task.artifacts(x=1, y=0)))
        #self.assertTrue(os.path.exists(_jobs[-1].task.artifacts(x=1, y=0)))
        #job.clear(x=1, y=0)
        #self.assertFalse(os.path.exists(job.artifacts))

    def test_task_artifact_custom(self):
        import os
        def f(x, y, path='/tmp/data_y{y}.txt'):
            with open(path.format(**locals()), 'w') as fh:
                fh.write(f'x={x}')
            return x
        def done(**kwargs):
            # This will work as long as there is a path argument
            path = kwargs['path'].format(**kwargs)
            return os.path.exists(path)
        def clear(**kwargs):
            from pantarei.helpers import rmd
            path = kwargs['path'].format(**kwargs)
            rmd(path)

        cache = Cache('/tmp/data')
        task = Task(f, cache=cache, done=done, clear=clear)
        task(x=1, y=0)
        self.assertTrue(task.done(x=1, y=0))
        task.clear(x=1, y=0)
        self.assertFalse(task.done(x=1, y=0))

    def test_task_tag(self):
        def f(x, debug=0):
            return x
        cache = Cache('/tmp/data')
        task = Task(f, cache=cache, tag='star')
        defaults = {'debug': True}
        task(x=1, **defaults)
        self.assertTrue(task.done(x=1, debug=True))
        import glob
        self.assertEqual(glob.glob('/tmp/data/f-star'), ['/tmp/data/f-star'])

    def test_browse(self):
        from pantarei import pantarei
        def f(x, debug):
            return x
        cache = Cache('/tmp/data')
        task = Task(f, cache=cache)
        db = pantarei.browse(path='/tmp/data')
        self.assertTrue(repr(db) == '')

        task(x=1, debug=False)
        db = pantarei.browse(path='/tmp/data')
        self.assertTrue(len(db) == 1)
        self.assertTrue(db['x'] == [1])
        self.assertTrue(db['debug'] == [False])

        # Check that order is preserved
        task(x=0, debug=False)
        db = pantarei.browse(path='/tmp/data')
        self.assertTrue(list(db['x']), [1, 0])

    # def test_syncer(self):
    #     from pantarei.helpers import mkdir
    #     from pantarei.syncer import rsync, Syncer

    #     mkdir('/tmp/data')
    #     with open('/tmp/data/hello.txt', 'w') as fh:
    #         fh.write('hello')

    #     with Syncer(source="/tmp/data",
    #                 dest="tmp",
    #                 dest_ssh="varda") as s:
    #         s.run()        
        
    def tearDown(self):
        from pantarei.helpers import rmd
        rmd('/tmp/data')

if __name__ == '__main__':
    unittest.main()
