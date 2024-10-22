# Pantarei

[![license](https://img.shields.io/pypi/l/atooms.svg)](https://en.wikipedia.org/wiki/GNU_General_Public_License)
[![pipeline status](https://framagit.org/coslo/pantarei/badges/master/pipeline.svg)](https://framagit.org/coslo/pantarei/-/commits/master)
[![coverage report](https://framagit.org/coslo/pantarei/badges/master/coverage.svg)](https://framagit.org/coslo/pantarei/-/commits/master)

A general-purpose workflow manager - because *everything* flows

## Quick start

Pantarei builds on three kinds of execution units:
- **functions** are stateless, Python callables
- **tasks** are stateful wrapped functions that cache execution results
- **jobs** are stateful wrapped tasks for distributed-memory parallel environments

To see it in action, say you have a Python function
```python
def f(x):
    import time
    time.sleep(2)
    return x
```

Wrap the function with a Task and call it with a range of arguments
```python
from pantarei import *

task = Task(f)
for x in [1, 2]:
    task(x=x)
```

The task's results are cached: a successive execution will just fetch the results
```python
results = task(x=1)
```

We wrap the task with a Job and submit jobs to a local scheduler (like SLURM)
```python
job = Job(task)
for x in [3, 4]:
    job(x=x)
```

Once the jobs are done, we can get the results (which are cached too)
```python
job.scheduler.wait()
results = job(x=3)
```

To see a summary of the jobs from the Python intepreter, add the following line at the end
```python
pantarei()
```

From the command line, you can check the state of the jobs by changing the execution mode ('safe', 'brave', 'timid') like this
```bash
pantarei=timid python script.py
```

## TODO

- [X] parametrize scheduler commands other than slurm
- [X] allow job submission within function
- [ ] add command line tool
- [ ] submit on remote cluster
- [ ] handle task dependencies
- [ ] add Workflow / Queue
- [ ] perhaps add signac-like view() or checkout() method to check out a view of cache as folders

## Mockups

Handle task dependencies
```python
def run(path):
    pass
def analyze(path):
    pass

# TODO: how to use results of dependent tasks?
run = Task(run, path='output.txt')
analyze = Task(analyze, depends=[run], path='output.txt')

for task in Workflow([run, analyze]):
    task()
```

Jobs inherit task dependencies
```python
run = Job(run, wall_time=24, cores=8)
analyze = Job(analyze, wall_time=1, cores=1)

for job in Workflow([run, analyze]):
    job()

# Wait for analyze job to end
job.scheduler.wait(analyze.fully_qualified_name())
```

Remote scheduler
```python
scheduler = Scheduler(host='login.m100.cineca.it', user='john_doe')
job = Job(f, scheduler=scheduler)
job(x=1)
job.scheduler.wait()
```

## Documentation

Check out the [tutorial]() for more examples and the [public API]() for full details.

## Installation

From pypi
```
pip install pantarei
```

## Contributing

Contributions to the project are welcome. If you wish to contribute, check out [these guidelines]().

## Authors

- Daniele Coslovich
