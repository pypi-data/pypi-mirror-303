import os
import unittest
import atooms.trajectory
import berni
try:
    import rumd
    import berni.rumd
    from atooms.backends.rumd import RUMD
    SKIP = False
except ImportError:
    SKIP = True

class Test(unittest.TestCase):

    def setUp(self):
        if SKIP:
            self.skipTest('missing RUMD')
        self.root = os.path.dirname(__file__)

    def test_(self):
        for model in ['kob_andersen', 'coslovich_pastore']:
            pot = berni.rumd.potential(model)

    def test_cp(self):
        import berni
        inp = berni.samples.get('coslovich_pastore-488db481cdac35e599922a26129c3e35.xyz')
        atooms.trajectory.TrajectoryXYZ(inp).copy(cls=atooms.trajectory.TrajectoryRUMD, fout='/tmp/1.xyz')
        model = 'coslovich_pastore'
        potentials = berni.rumd.potential(model)
        backend = RUMD('/tmp/1.xyz', potentials=potentials)
        epot_0 = backend.system.potential_energy(per_particle=True)

        model = 'coslovich_pastore'
        model = berni.get(model)
        model['cutoff'][0]['type'] = 'linear_cut_shift'
        model['cutoff'][0]['parameters']['rcut'] = model['cutoff'][0]['parameters']['rspl']
        model['cutoff'][0]['parameters'].pop('rspl')
        with atooms.trajectory.Trajectory(inp) as th:
            s = th[0]
            s.species_layout = 'F'
            s.interaction = berni.f90.Interaction(model)
            epot_1 = s.potential_energy(per_particle=True)
        self.assertLess(abs(epot_0 - epot_1), 1e-6)
        import os
        os.system(f'rm -f {inp}')

    def test_ka(self):
        inp = berni.samples.get('kob_andersen-8f4a9fe755e5c1966c10b50c9a53e6bf.xyz')
        atooms.trajectory.TrajectoryXYZ(inp).copy(cls=atooms.trajectory.TrajectoryRUMD, fout='/tmp/1.xyz')
        model = 'kob_andersen'
        potentials = berni.rumd.potential(model)
        backend = RUMD('/tmp/1.xyz', potentials=potentials)
        epot_0 = backend.system.potential_energy(per_particle=True)
        model = 'kob_andersen'
        with atooms.trajectory.Trajectory(inp) as th:
            s = th[0]
            s.species_layout = 'F'
            s.interaction = berni.f90.Interaction(model)
            epot_1 = s.potential_energy(per_particle=True)
        self.assertLess(abs(epot_0 - epot_1), 1e-6)
        import os
        os.system(f'rm -f {inp}')

    def tearDown(self):
        import os
        os.system('rm -f /tmp/1.xyz')


if __name__ == '__main__':
    unittest.main()
