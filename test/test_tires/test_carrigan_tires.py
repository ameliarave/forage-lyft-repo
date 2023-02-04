#!/usr/bin/env python3
import unittest
from datetime import datetime
from car.tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_array = [0, 0, 0.9, 0]
        tires = CarriganTire(tire_array)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_array = [0.1, 0.2, 0.3, 0.4]
        tires = CarriganTire(tire_array)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()