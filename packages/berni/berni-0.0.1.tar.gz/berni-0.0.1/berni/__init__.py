"""
Database of interaction models for classical molecular dynamics
and Monte Carlo simulations
"""

import os
import glob
import json
import tempfile
import shutil
from copy import deepcopy
from tinydb import Query
from tinydb import TinyDB as _TinyDB
from tinydb.storages import MemoryStorage
from .helpers import _wget, pprint
from .schema import schema_version
from . import _schemas


class TinyDB(_TinyDB):

    default_storage_class = MemoryStorage
    default_table_name = 1
    _get_payload = None
    _str_kwargs = {'include': ['name']}

    def get(self, name, **kwargs):
        """Get the payload associated to the qualified name"""
        return self._get_payload(self, name, **kwargs)

    def fields(self, merge=set.union):
        """Return fields of database"""
        cols = None
        for entry in self:
            if cols is None:
                cols = set(entry.keys())
            else:
                cols = merge(cols, set(entry.keys()))
        return sorted(list(cols))

    def pprint(self, include=None, cond=None, sort_by=None,
               max_rows=20, max_len=140, file=None):
        kwargs = locals()
        kwargs.pop('cond')
        kwargs.pop('self')
        if cond is None:
            pprint(self.all(), **kwargs)
        else:
            pprint(self.search(cond), **kwargs)

    def __str__(self):
        from .helpers import pprint
        from io import StringIO
        with StringIO() as io:
            pprint(self.all(), **self._str_kwargs, file=io)
            txt = io.getvalue()
        return txt

def _get_model(db, name, schema_version=1):
    """
    Return the model matching the qualified name  `name`

    The qualified name has the form <model_name>[-<variant>]
    """
    # Look for a single match
    query = Query()
    db.default_table_name = schema_version
    entry = db.search(query.name == name)
    if len(entry) == 1:
        # Get the actual payload
        return deepcopy(entry[0]['_model'])
    if len(entry) == 0:
        raise KeyError(f'Model {name} not found with schema {schema_version}')
    if len(entry) > 1:
        raise KeyError(f'Multiple models {name} found')

def _get_sample(db, name, output_path=None):
    """
    Get a copy of sample `name` and return the actual path to it
    """
    query = Query()
    entry = db.search((query.name == name))[0]

    if output_path is None:
        tmpdir = tempfile.mkdtemp()
        output_path = os.path.join(tmpdir, name)

    if 'url' in entry:
        _wget(entry['url'], tmpdir)
    else:
        url = os.path.join(_samples, entry['name'])
        shutil.copy(url, output_path)
    return output_path


_root = os.path.dirname(__file__)
_samples = os.path.join(_root, 'samples')
schemas = {1: _schemas.m1, 2: _schemas.m2}
models = TinyDB()
samples = TinyDB()
models._str_kwargs = {'include': ['name', 'reference'], 'sort_by': 'name'}
samples._str_kwargs = {'include': ['name', 'model'], 'sort_by': 'name'}
# Monkey patch TinyDBs with custom getters
models._get_payload = _get_model
samples._get_payload = _get_sample

# Aliases (get and model) for backward compatibility
def model(model, schema_version=1):
    return models.get(model, schema_version=schema_version)


get = model

# Store models
def _store_models(models):
    """Store models in the global database"""
    for f in glob.glob(f'{_root}/models/*.json'):
        with open(f) as fh:
            model = json.load(fh)
        sv = schema_version(model)
        # if 'variant' not in model['metadata']:
        #     model['metadata']['variant'] = 0
        # Store model in database table of this schema version
        table = models.table(sv)
        metadata = model.pop('metadata')
        table.insert({**metadata, '_model': model})

# Store samples
def _store_samples(samples):
    """Store samples in the global database"""
    for path in glob.glob(f'{_samples}/*.json'):
        with open(path) as fh:
            data = json.load(fh)
            samples.insert(data)


_store_models(models)
_store_samples(samples)


# Convenience export function for backends
def export(model, backend, *args, **kwargs):
    """
    Export `model` to suitable object for `backend`, passing
    additional optional arguments to the backend
    """
    from . import f90, rumd
    _map = {
        'f90': f90,
        'rumd': rumd
    }
    return _map[backend].export(model, *args, **kwargs)


# Potentials and cutoffs
from inspect import getmembers, isfunction, isclass
from .helpers import _objdict
from . import _potentials
from . import _cutoffs

potentials = _objdict()
for name, func in getmembers(_potentials, isfunction):
    potentials[name] = func

cutoffs = _objdict()
for name, cls in getmembers(_cutoffs, isclass):
    if name != '_objdict':
        cutoffs[name] = cls

def potential(name):
    return potentials[name]

def cutoff(name):
    return cutoffs[name]
