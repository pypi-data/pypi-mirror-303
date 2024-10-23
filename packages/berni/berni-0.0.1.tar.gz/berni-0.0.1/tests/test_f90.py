import os
import unittest
from berni import models, samples
from atooms.trajectory import Trajectory
from atooms.system import System, Particle, Cell
from berni.f90 import Interaction


class Test(unittest.TestCase):

    def setUp(self):
        self.fileinp = os.path.join(os.path.dirname(__file__), '../berni/samples/lennard_jones-13ce47602b259f7802e89e23ffd57f19.xyz')
        self.trajectory = Trajectory(self.fileinp)

    def test_collinear(self):
        model = models.get("lennard_jones")
        particles = [Particle(position=[0.0, 0.0, 0.0], species=1),
                     Particle(position=[1.0, 0.0, 0.0], species=1),
                     Particle(position=[2.0, 0.0, 0.0], species=1)]
        cell = Cell([10., 10., 10.])
        system = System(particles, cell)
        system.interaction = Interaction(model)
        self.assertAlmostEqual(system.potential_energy(), -0.01257276409199999)

    def test_ntw(self):
        trajectory = Trajectory(os.path.join(os.path.dirname(__file__), '../berni/samples/coslovich_pastore-488db481cdac35e599922a26129c3e35.xyz'))
        system = trajectory[0]
        system.species_layout = 'F'
        system.interaction = Interaction('coslovich_pastore')
        self.assertAlmostEqual(system.potential_energy(per_particle=True), -6.0295, places=4)

    def tearDown(self):
        self.trajectory.close()


if __name__ == '__main__':
    unittest.main()
