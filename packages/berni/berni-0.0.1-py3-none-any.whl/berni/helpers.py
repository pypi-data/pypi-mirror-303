import os
import shutil
import hashlib
from .schema import schema_version


def pprint(rows, include=None, sort_by=None, max_rows=20, max_len=140, file=None):
    """Pretty print `rows` (a list of dicts)"""

    def _tabular(data, max_len=max_len):
        """General function to format `data` list in tabular table"""
        # Predict formatting
        lens = [0 for _ in range(len(data[0]))]
        for entry in data:
            for i, value in enumerate(entry):
                lens[i] = max(lens[i], len(str(value)))
        fmts = [f'{{:{lens[i]}s}}' for i in range(len(lens))]
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

    # Format and sort the data
    if include is None:
        columns = set([e for e in rows[0] if not e.startswith('_')])
        for entry in rows:
            new_columns = set([e for e in entry if not e.startswith('_')])
            columns = set.union(columns, new_columns)
        columns = sorted(columns)
    else:
        columns = include

    if sort_by is not None:
        if not (isinstance(sort_by, list) or isinstance(sort_by, tuple)):
            sort_by = [sort_by]
        rows = sorted(rows[1:], key=lambda x: [x[_] for _ in sort_by])

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

class _objdict(dict):

    """Boots a dict with object-like attribute accessor"""

    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]

# TODO: clean up and restore the functions below, for internal use

# To add a model
# def add_model_json(path):
#     """
#     If `path` is a directory, add all json files in there to the
#     global `database`. If `path` ends with `json`, it will be assumed
#     to be match one or multiple json files (ex. `*.json`).
#     """
#     import json
#     import glob
#     if path.endswith('json'):
#         search_path = glob.glob(path)
#     else:
#         search_path = glob.glob('{}/*.json'.format(path))

#     for _path in search_path:
#         # Read json file
#         with open(_path) as fh:
#             try:
#                 model = json.load(fh)
#             except (ValueError, json.decoder.JSONDecodeError):
#                 print('Error reading file {}'.format(_path))
#                 raise

#         # By default, the model name is the file basename (stripped of .json)
#         if 'name' not in model:
#             name = os.path.basename(_path)[:-5]
#             model['name'] = '-'.join([entry.capitalize() for entry in name.split('_')])

#         yield model

# To add a sample
# def update(pretend=False):
#     for sample in samples():
#         model, path = sample["model"], sample["path"]
#         sample = {k: sample[k] for k in sample if k not in ["model", "path"]}
#         if path.startswith('http'):
#             store(path, model, pretend=pretend, **sample)
#         else:
#             store(os.path.join(_storage, path), model, pretend=pretend, **sample)


# def _store(path, model, version=0, format=None, notes="", state="", pretend=False, **kwargs):
#     """
#     Keyword arguments can be added to describe the thermodynamic state
#     of the system.
#     """
#     import tempfile
#     _storage_path = '{model}-{variant}-{md5_hash}'

#     # Set paths: storage_path is what goes in the db
#     if path.startswith('http'):
#         tmpdir = tempfile.mkdtemp()
#         basename = os.path.basename(path)
#         _wget(path, tmpdir)
#         local_path = os.path.join(tmpdir, basename)
#     else:
#         local_path = path

#     # We now have a local copy in local_path, get the md5 hash
#     with open(local_path, "rb") as fh:
#         data = fh.read()
#         md5_hash = hashlib.md5(data).hexdigest()
#         extension = os.path.splitext(local_path)[-1]

#     _locals = {}
#     _locals.update(kwargs)
#     _locals['md5_hash'] = md5_hash
#     _locals['model'] = model
#     _locals['version'] = version
#     storage_path = _storage_path.format(**_locals)

#     # Add the entry and its metadata
#     entry = {}
#     entry.update(**kwargs)
#     entry.update({
# 	"model": model,
#         "version": version,
#         "md5_hash": md5_hash,
#         "path": path,
# 	"format": format,
#     })
#     if not path.startswith('http'):
#         entry["path"] = storage_path + extension

#     if pretend:
#         print(os.path.join(_storage, storage_path))
#         return

#     from atooms.core.utils import mkdir
#     mkdir(os.path.dirname(os.path.join(_storage, storage_path)))

#     # Store json file
#     with open(os.path.join(_storage, storage_path + ".json"), 'w') as f:
#         json.dump(entry, f, indent=4)

#     # Store the json file in the storage/ (or samples/).
#     # I would like to use a descriptive path name, but it could be
#     # that the kwargs are not enough to distinguish them.
#     # So I use the md5 hash itself, but prefixed with model name and
#     # version, to have ar least a feeling of what is it.

#     # TODO: issue when having two entries that point to the same file,
#     # but one is a local file reference (within the repo) and the
#     # other one is via the url (on framagit).
#     # But in principle, one could have multiple ways to get to a sample (for redundancy)
#     # If they are all mapped to the same .json file, it does not work.
#     # 1) add a warning that we are overwriting
#     # 2) perhaps add some reference in the path to the storage (file or http)
#     # Actually, there could be multiple instances over the network,
#     # one would need to hash the url!
#     if not path.startswith('http'):
#         with open(os.path.join(_storage, entry["path"]), "wb") as fh:
#             fh.write(data)
