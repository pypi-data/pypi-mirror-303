"""
Helper functions
"""

import sys
import os
import shutil
import hashlib
import inspect

def arguments(func):
    """
    Return arguments without default value (positional) and with
    default value (keyword) in function `func`
    """
    signature = inspect.signature(func)
    args = tuple(param.name
                 for param in signature.parameters.values()
                 if param.default is param.empty)
    kwargs = {param.name: param.default
              for param in signature.parameters.values()
              if param.default is not param.empty}
    return args, kwargs

def actual_kwargs(func, *args, **kwargs):
    """Return all the arguments of a function as keyword arguments."""
    signature = inspect.signature(func)
    arg_names = tuple(param.name
                      for param in signature.parameters.values()
                      if param.default is param.empty)
    # TODO: check if we passed a keyword argument with the same value as default
    # Default keyword arguments
    # actual_args = {param.name: param.default
    #               for param in signature.parameters.values()
    #               if param.default is not param.empty}
    actual_args = {}
    actual_args.update({name: arg for name, arg in zip(arg_names, args)})
    actual_args.update(kwargs)
    return actual_args

def all_actual_kwargs(func, *args, **kwargs):
    """Return all the arguments of a function as keyword arguments."""
    signature = inspect.signature(func)
    arg_names = tuple(param.name
                      for param in signature.parameters.values()
                      if param.default is param.empty)
    # TODO: check if we passed a keyword argument we the same value as default
    # Default keyword arguments
    actual_args = {param.name: param.default
                   for param in signature.parameters.values()
                   if param.default is not param.empty}
    # actual_args = {}
    actual_args.update({name: arg for name, arg in zip(arg_names, args)})
    actual_args.update(kwargs)
    return actual_args

def actual_kwargs(signature_args, signature_kwargs, args, kwargs):
    """Return all the arguments of a function as keyword arguments."""
    # TODO: check if we passed a keyword argument with the same value as default
    actual_args = {}
    actual_args.update({name: arg for name, arg in zip(signature_args, args)})
    actual_args.update(kwargs)
    return actual_args

def all_actual_kwargs(signature_args, signature_kwargs, args, kwargs):
    """Return all the arguments of a function as keyword arguments."""
    actual_args = signature_kwargs
    actual_args.update({name: arg for name, arg in zip(signature_args, args)})
    actual_args.update(kwargs)
    return actual_args

def mkdir(dirname):
    """
    Create a directory `dirname` or a list `dirname` of directories,
    silently ignoring existing directories.

    This is just a wrapper to `os.makedirs`. All intermediate
    subdirectories are created as needed.
    """
    import os
    if dirname is None:
        return
    if isinstance(dirname, str):
        dirs = [dirname]
    else:
        dirs = dirname

    for dd in dirs:
        try:
            os.makedirs(dd)
        except OSError:
            pass

def rmd(files):
    """Totally silent wrapper to shutil.rmtree."""
    import shutil
    try:
        shutil.rmtree(files)
    except BaseException:
        pass

def rmf(files):
    """
    Remove `files` without complaining.

    The variable `files` can be a list or tuple of paths or a single
    string parseable by glob.glob().
    """
    import glob
    try:
        # This a single pattern
        for pathname in glob.glob(files):
            try:
                os.remove(pathname)
            except OSError:
                # File does not exists or it is a folder
                pass
    except (TypeError, AttributeError):
        # This is a list
        for pathname in files:
            try:
                os.remove(pathname)
            except OSError:
                # File does not exists or it is a folder
                pass

def serialize_kwargs(kwargs):
    """Return a string from the `kwargs` dictionary"""
    args = []
    for key in kwargs:
        if isinstance(kwargs[key], str):
            args.append(f'{key}="{kwargs[key]}"')
        else:
            args.append(f'{key}={kwargs[key]}')
    return ','.join(args)

def tag_function(f, name, doc=None):
    """Tag a function with `name` suffix"""
    from types import FunctionType
    func = FunctionType(f.__code__, f.__globals__, f.__name__ + '_' + name,
                        f.__defaults__, f.__closure__)
    if doc is not None:
        # func.__doc__ = '\n'.join((func.__doc__, doc))
        func.__doc__ = doc
    return func

def pprint(rows, columns=None, ignore=(), sort_by=None, max_rows=100, file=sys.stdout, max_width=100):
    """Pretty print `rows` (a list of dicts)"""

    def _tabular(data, max_len=max_width):
        """General function to format `data` list in tabular table"""

        # Predict formatting
        col_lens = [len(entry) for entry in data[0]]
        lens = [0 for _ in range(len(data[0]))]
        for entry in data:
            for i, value in enumerate(entry):
                lens[i] = max(lens[i], len(str(value)))

        if sum(lens) > max_len:
            # Squeeze: try to to fit by fitting to column widths
            for i in range(len(lens)):
                if lens[i] > col_lens[i] and lens[i] > 8:
                    lens[i] = col_lens[i]+1

        # TODO: add some padding indication
        fmts = [f'{{:{lens[i]}.{lens[i]}s}}' for i in range(len(lens))]
        fmt = ' '.join(fmts)

        # Store list of lines
        lines = []
        lines.append(fmt.format(*data[0]))
        lines.append('-'*(sum(lens) + len(lens) - 1))
        for entry in data[1:]:
            entry = [str(_) for _ in entry]
            lines.append(fmt.format(*entry))
            if len(lines) > max_rows and max_rows > 0:
                lines.append(f'... {len(data) - max_rows} entries not shown')
                break

        # Limit columns
        if sum(lens) > max_len:
            for i, line in enumerate(lines):
                if i < 2:
                    fill = '     '
                else:
                    fill = ' ... '
                lines[i] = line[:max_len//2] + fill + line[sum(lens) - max_len//2:]
        return lines

    if len(rows) == 0:
        return ''

    # Format and sort the data
    row = rows[0]
    if hasattr(row, 'keys'):
        keys = row.keys()
    else:
        keys = row.dtype.names
    # TODO: fix this, with structured arrays the column order must be the prescribed one
    if columns is None:
        columns = set([e for e in keys if not e.startswith('__')])
        for entry in rows:
            new_columns = set([e for e in entry if not e.startswith('__')])
            columns = set.union(columns, new_columns)
        columns = sorted(columns)

    # Ignore some columns
    for ignored in ignore:
        if ignored in columns:
            columns.pop(columns.index(ignored))

    if sort_by is not None:
        if not (isinstance(sort_by, list) or isinstance(sort_by, tuple)):
            sort_by = [sort_by]
        rows = sorted(rows, key=lambda x: [x[_] for _ in sort_by])

    # Tabularize lines and join them
    rows = [columns] + [[str(entry.get(key)) for key in columns] for entry in rows]
    lines = _tabular(rows)
    print('\n'.join(lines), file=file)

def _wget(url, output_dir):
    """Like wget on the command line"""
    try:
        from urllib.request import urlopen  # Python 3
    except ImportError:
        from urllib2 import urlopen  # Python 2

    basename = os.path.basename(url)
    output_file = os.path.join(output_dir, basename)
    response = urlopen(url)
    length = 16*1024
    with open(output_file, 'wb') as fh:
        shutil.copyfileobj(response, fh, length)

# TODO: do not rely on entry
def copy(entry, path='/tmp/{path}', root=''):
    """Get a copy of `path` in the samples database and return the path to it"""
    import tempfile

    # Handle output path
    if path is None:
        # Output path is a temporary directory
        outdir = tempfile.mkdtemp()
        basename = os.path.basename(entry['path'])
        path = os.path.join(outdir, basename)
    else:
        # Interpolate path with entry fields
        path = path.format(**entry)
        outdir = os.path.dirname(path)

    # Now copy
    if entry['path'].startswith('http'):
        # Over the network
        _wget(entry['path'], outdir)
    else:
        # Local storage
        mkdir(os.path.dirname(path))
        if entry['path'].startswith('/'):
            # Absolute path, so ignore root variable
            shutil.copy(entry['path'], path)
        else:
            # Path is relative to root, most likely database folder
            shutil.copy(os.path.join(root, entry['path']), path)

    return path

def tipify(s):
    """
    Convert a string into the best matching type.

    Examples
    --------

    .. code-block:: python

        type(tipify("2.0")) is float
        type(tipify("2")) is int
        type(tipify("t2")) is str
        map(tipify, ["2.0", "2"])

    The only risk is if a variable is required to be float,
    but is passed without dot.
    """
    if '_' in s:
        return s
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s

def debug_stacks(stacks):
    import dill
    # DEBUG Try to fix...
    # dill.settings['recurse'] = True
    # print(s.frame.f_locals)
    print('******')
    for i, ss in enumerate(stacks):
        print('-'*50)
        print('Level:', i)
        import pprint
        print(ss.frame)
        pprint.pprint(ss.frame.f_locals)
        try:
            dill.dump_module(f'/tmp/s{i}.pkl', module=inspect.getmodule(ss.frame.f_code), refimported=False)
        except TypeError:
            print('*WARNING*: cannot dill this frame!')
        print('Source:')
        print(dill.source.getsource(ss.frame.f_code))
        print()
        print('Trace:')
        with dill.detect.trace():
            dill.dumps(ss.frame.f_code)
        print()
