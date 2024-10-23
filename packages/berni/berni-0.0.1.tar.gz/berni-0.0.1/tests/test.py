#!/usr/bin/env python

import os
import unittest
from berni import models, samples, schema

root = os.path.dirname(__file__)

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def _compare_data(self, ref, copy):
        with open(ref) as fh:
            data = fh.read()
        with open(copy) as fh:
            data_copy = fh.read()
        self.assertEqual(data, data_copy)

    def test_grammar(self):
        models.all()
        models.get("lennard_jones")
        samples.all()
        samples.get("lennard_jones-5cc3b80bc415fa5c262e83410ca65779.xyz")

    def test(self):
        sample = samples.get("lennard_jones-5cc3b80bc415fa5c262e83410ca65779.xyz")
        raw = root + '/../berni/samples/lennard_jones-5cc3b80bc415fa5c262e83410ca65779.xyz'
        self._compare_data(raw, sample)

    def test_convert(self):
        m = {
            "metadata": {'name': 'lj'},
            "potential": [
                {
                    "type": "lennard_jones",
                    "parameters": {"sigma": [[1.0, 0.8], [0.8, 0.88]],
                                   "epsilon": [[1.0, 1.5], [1.5, 0.5]]}
                }
            ],
            "cutoff": [
                {
                    "type": "cut_shift",
                    "parameters": {"rcut": [[2.5, 2.0], [2.0, 2.2]]}
                }
            ]
        }
        n = {'potential': [{'cutoff': {'parameters': {'1-1': {'rcut': 2.5},
                                                      '1-2': {'rcut': 2.0},
                                                      '2-2': {'rcut': 2.2}},
                                       'type': 'cut_shift'},
                            'parameters': {'1-1': {'epsilon': 1.0, 'sigma': 1.0},
                                           '1-2': {'epsilon': 1.5, 'sigma': 0.8},
                                           '2-2': {'epsilon': 0.5, 'sigma': 0.88}},
                            'type': 'lennard_jones'}],
             "metadata": {'name': 'lj'},
             }
        self.assertEqual(m, schema._convert(m, 1))
        self.assertEqual(n, schema._convert(m, 2))

    def test_schemas(self):
        from jsonschema import validate
        from berni import models

        for version in [1, ]:
            models.default_table_name = version
            for model in models:
                # Moving the payload to _model means that we cannot
                # use model right away, we must get it
                validate(instance=models.get(model['name']),
                         schema=schema.schemas[version])

    def test_storage(self):
        import glob
        from berni import Query
        query = Query()
        sample = samples.search((query.model == 'lennard_jones') &
                                (query.density == 1.0))[0]
        name = sample['name']
        self.assertTrue(len(samples.get(name)) > 0)

    def test_pprint(self):
        with open('/dev/null', 'w') as null:
            models.pprint(file=null)
            models.pprint(include=['name', 'doi'], file=null)

    def test_potentials(self):
        from berni import potentials
        for f in potentials.values():
            f(0.9)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
