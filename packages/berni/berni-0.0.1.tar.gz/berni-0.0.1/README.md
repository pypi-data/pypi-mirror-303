Berni
=====

[![pypi](https://img.shields.io/pypi/v/berni.svg)](https://pypi.python.org/pypi/berni/)
[![version](https://img.shields.io/pypi/pyversions/berni.svg)](https://pypi.python.org/pypi/berni/)
[![license](https://img.shields.io/pypi/l/berni.svg)](https://en.wikipedia.org/wiki/GNU_General_Public_License)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/git/https%3A%2F%2Fframagit.org%2Fcoslo%2Fberni/HEAD?labpath=docs%2Findex.ipynb)
[![pipeline](https://framagit.org/coslo/berni/badges/master/pipeline.svg)](https://framagit.org/coslo/berni/badges/master/pipeline.svg)
[![coverage report](https://framagit.org/coslo/berni/badges/master/coverage.svg?job=test:f90)](https://framagit.org/coslo/berni/-/commits/master)

A database of interaction models for classical molecular dynamics and Monte Carlo simulations.

Quick start
-----------

Print all the available models
```python
import berni
for model in berni.models:
    print(model["name"])
```
```
gaussian_core
coslovich_pastore
bernu_hiwatari_hansen_pastore
lennard_jones
kob_andersen
roux_barrat_hansen
grigera_cavagna_giardina_parisi
harmonic_spheres
kob_andersen_2
dellavalle_gazzillo_frattini_pastore
wahnstrom
kob_andersen
coslovich_pastore
```

Get a model
```python
berni.models.get("lennard_jones")
```

Print all the available samples
```python
for sample in berni.samples():
    print(sample["path"])
```
```
lennard_jones-13ce47602b259f7802e89e23ffd57f19.xyz
grigera_cavagna_giardina_parisi-0ac97fa8c69c320e48bd1fca80855e8a.xyz
coslovich_pastore-488db481cdac35e599922a26129c3e35.xyz
lennard_jones-5cc3b80bc415fa5c262e83410ca65779.xyz
kob_andersen-8f4a9fe755e5c1966c10b50c9a53e6bf.xyz
bernu_hiwatari_hansen_pastore-f61d7e58b9656cf9640f6e5754441930.xyz
```

Get a local copy of a Lennard-Jones fluid sample
```python
local_file = berni.models.get("lennard_jones-5cc3b80bc415fa5c262e83410ca65779.xyz")
```

The `local_file` can then be used to start a simulation or further analysis.

Documentation
-------------
Check out the [documentation](https://coslo.frama.io/berni) for full details.

Installation
------------
Clone the code repository and install from source
```
git clone https://framagit.org/coslo/berni.git
cd sample
make install
```

Install `berni` with pip
```
pip install berni
```

Contributing
------------
Contributions to the project are welcome. If you wish to contribute, check out [these guidelines](https://framagit.org/coslo/berni/-/blob/master/CONTRIBUTING.md).

Authors
-------
Daniele Coslovich: https://www.units.it/daniele.coslovich/
