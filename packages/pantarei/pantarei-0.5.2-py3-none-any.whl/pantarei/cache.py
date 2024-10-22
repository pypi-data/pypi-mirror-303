"""
Cache
"""
import os
import pickle
import yaml
import numpy
from .helpers import mkdir, rmd

# TODO: use something better than pickle, like marshmallow, to dump data

def _itemize(data):
    """Itemize numpy arrays in data"""
    if isinstance(data, dict):
        # Turn all ndarrays into lists
        new_data = {}
        for key in data:
            if isinstance(data[key], numpy.ndarray):
                new_data[key] = numpy.ndarray.tolist(data[key])
            elif type(data[key]).__module__ == 'numpy':
                # Could not find a better way to check any dytpe
                new_data[key] = data[key].item()
            else:
                new_data[key] = data[key]
        return new_data
    # If data is an ndarray, turn it to a list
    if isinstance(data, numpy.ndarray):
        return numpy.ndarray.tolist(data)
    if type(data).__module__ == 'numpy':
        # Could not find a better way to check any dytpe
        return data.item()
    # Just return data if all else fails
    return data

class Cache:
    """
    Cache results of function evaluation on the basis of its name and
    keyword arguments
    """

    def __init__(self, path):
        """
        :param path: path to cache folder
        """
        self.path = path

    def _storage(self, name):
        return os.path.join(self.path, name)

    def setup(self, name, **kwargs):
        """Setup the cache for `name` with `kwargs`"""
        path = self._storage(name)
        mkdir(path)
        with open(os.path.join(path, 'arguments.pkl'), 'wb') as fh:
            pickle.dump(kwargs, fh)
        # For quick inspection, we also provide a yaml file
        # which will be ignored by default by parsers
        with open(os.path.join(path, '.arguments.yaml'), 'w') as fh:
            yaml.dump(_itemize(kwargs), fh)

    def setup_any(self, entry, name, kwargs):
        """Setup the cache for `name` with `kwargs`"""
        import os
        path = self._storage(name)
        mkdir(path)
        with open(os.path.join(path, f'{entry}.pkl'), 'wb') as fh:
            pickle.dump(kwargs, fh)
        # For quick inspection, we also provide a yaml file
        # which will be ignored by default by parsers
        with open(os.path.join(path, f'.{entry}.yaml'), 'w') as fh:
            yaml.dump(_itemize(kwargs), fh)
            
    def write(self, name, results):
        """Write the function cache results for `name`"""
        path = self._storage(name)
        with open(os.path.join(path, 'results.pkl'), 'wb') as fh:
            pickle.dump(results, fh)
        with open(os.path.join(path, '.results.yaml'), 'w') as fh:
            # Itemize all numpy arrays
            yaml.dump(_itemize(results), fh)

    def read(self, name):
        """Return the function cache results"""
        path = self._storage(name)
        with open(os.path.join(path, 'results.pkl'), 'rb') as fh:
            results = pickle.load(fh)
        return results

    def found(self, name):
        """Return True is `name` if found in cache"""
        path = self._storage(name)
        return os.path.exists(os.path.join(path, 'results.pkl'))

    def is_setup(self, name):
        """Return True is `name` has been set up in cache"""
        path = self._storage(name)
        return os.path.exists(os.path.join(path, 'arguments.pkl'))
    
    def clear(self, name):
        """Clear cache for `name`"""
        rmd(self._storage(name))


default_cache = Cache('.pantarei')
