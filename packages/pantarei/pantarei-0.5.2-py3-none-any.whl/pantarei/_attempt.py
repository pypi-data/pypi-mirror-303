"""."""
def submit_attempt(func, *args, **kwargs):
    """."""
    import pickle
    import inspect
    import subprocess
    import traceback

    stacks = inspect.stack()
    for i in range(len(stacks)):
        s = stacks[i]
        print('STACK', i+1, 'out of ', len(stacks))
        print('__code' in s.frame.f_locals)
        print(s.filename)
        print(s.frame.f_code, s.frame.f_code.co_firstlineno, s.frame.f_lineno, s.frame.f_code.co_filename)
        # print(s.frame.f_locals)
        i = s.frame.f_code.co_firstlineno - 1
        j = s.frame.f_lineno - 1
        print(i, j, '-'*50)
        if s.frame.f_code.co_filename != '<stdin>':
            with open(s.frame.f_code.co_filename) as fh:
                for _, line in enumerate(fh):
                    if i <= _ < j:
                        print(_, '>>', line.strip('\n'))
                    elif i-3 <= _ <= j+3:
                        print(_, '  ', line.strip('\n'))
        else:
            print('===== STDIN =====')
        print('-'*50)
        print()

    # frm = inspect.stack()[level]
    # mod = inspect.getmodule(frm[0])
    # s = inspect.stack()[2]
    s = stacks[-1]
    print('+++++', s.frame.f_code.co_filename, '__code' in s.frame.f_locals)

    PIK = "pickle.dat"

    # Remove modules
    # TODO: ignore callables like task and job instances
    full = s.frame.f_locals
    print('+++++', s.frame.f_code.co_filename, '__code' in s.frame.f_locals)
    from .job import Job
    from .task import Task
    funcs = {key: full[key].__module__ for key in full if (callable(full[key]) and
                                                           not isinstance(full[key], Task) and
                                                           not isinstance(full[key], Job) and
                                                           full[key].__module__ != '__main__')}

    data = {key: full[key] for key in full if (type(full[key]) != type(inspect) and
                                               not callable(full[key]) and
                                               not key.startswith('__') and
                                               not isinstance(full[key], Task) and
                                               not isinstance(full[key], Job) and
                                               key != 'code' and
                                               key != 'main_globals')}
    # for key in data:
    #     print(key, data[key])
    for key in data:
        print('----', key, type(full[key]), callable(full[key]), key.startswith('__'))
        with open('/tmp/1.pkl', "wb") as f:
            try:
                pickle.dump(full[key], f)
            except:
                print('no pickle', key, full[key])

    mods = {key: full[key] for key in full if (type(full[key]) != type(inspect))}

    with open(PIK, "wb") as f:
        pickle.dump(data, f)

    print('+++++', s.frame.f_code.co_filename, '__code' in s.frame.f_locals)
    code = ''
    if '__code' not in s.frame.f_locals:
        print('====== NOT found __code!')
        assert s.frame.f_code.co_filename != '<stdin>'
        i = s.frame.f_code.co_firstlineno - 1
        j = s.frame.f_lineno - 1
        with open(s.frame.f_code.co_filename) as fh:
            for _, line in enumerate(fh):
                # if i <= _ <= j:
                if i <= _ < j:
                    code += line
    else:
        print('====== USING __code!')
        for line in s.frame.f_locals['__code'].decode().split('\n'):
            # TODO: this is fragile
            if line.strip().startswith('job('):
                continue
            code += line + '\n'

    args = []
    for key in kwargs:
        if isinstance(kwargs[key], str):
            args.append(f'{key}="{kwargs[key]}"')
        else:
            args.append(f'{key}={kwargs[key]}')
    kwargs = ','.join(args)

    imports = []
    funcs_paste = []
    for key in funcs:
        if key.startswith('_'):
            continue
        # print('IMPRT ', key, funcs[key])
        # These functions are defined locally in the session, we paste their code
        # TODO: it may duplicate the {code} below, we can fix it
        # One option is to store the bytecode and then import it
        # Or just simply accept that functions must be in modules.
        # if funcs[key] == '__main__': continue
        imports.append(f'from {funcs[key]} import {key}')
    imports = '\n'.join(imports)

    # Funcs to paste from main
    # TODO: it does not work, inspect fails on live sessions,
    # they must be in a file when called
    func_bodies = []
    for key in full:
        if callable(full[key]) and full[key].__module__ == '__main__':
            try:
                func_bodies.append(inspect.getsource(full[key]))
            except OSError:
                print('failed with source of', full[key])
    func_bodies = '\n'.join(func_bodies)

    script = f"""\
#!/usr/bin/env python
__name__ = '__main__'
import sys
import pickle
sys.path.append('.')
{imports}

with open("{PIK}", "rb") as __fh:
    globals().update(pickle.load(__fh))
{code}
{func.__name__}({kwargs})
"""
    # TODO: we should return the results (pickling it)
    print(script)
    # subprocess.run(f"""sbatch <<'EOF'
    # print(f"""sbatch <<'EOF'
    subprocess.run(f"""python - <<'EOF'
{script}
EOF""", shell=True)
    # print(f"""python - <<EOF
# {s.frame.f_locals['__code'].decode()}
# EOF""")
