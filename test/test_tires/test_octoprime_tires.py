import unittest
from car.tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_array = [0.75, 0.75, 0.75, 0.75]
        tires = OctoprimeTire(tire_array)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_array = [0.74, 0.75, 0.75, 0.75]
        tires = OctoprimeTire(tire_array)
        self.assertFalse(tires.needs_service()) 

if __name__ == '__main__':
    unittest.main()