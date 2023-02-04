#!/usr/bin/env python3
import unittest
from datetime import datetime
from car_factory import CarFactory


class TestCarriganTire(unittest.TestCase):
    def test_tires_should be serviced(self):
        tire_array = [0, 0, 0.9, 0]
        tires = CarriganTire(tire_array)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_array = [0.1, 0.2, 0.3, 0.4]
        tires = CarriganTire(tire_array)
        self.assertFalse(tires.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_array = [0.75, 0.75, 0.75, 0.75]
        tires = OctoprimeTire(tire_array)
        self.assertTrue(tire.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_array = [0.74, 0.75, 0.75, 0.75]
        tires = OctoprimeTire(tire_array)
        self.assertFalse(tires.needs_service()) 

class TestCalliope(unittest.TestCase):     
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        factory = CarFactory()
        car = factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        current_date = today

        factory = CarFactory()
        car = factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        current_date = datetime.today().date()

        factory = CarFactory()
        car = factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        current_date = datetime.today().date()

        factory = CarFactory()
        car = factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        factory = CarFactory()
        car = factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        factory = CarFactory()
        car = factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        factory = CarFactory()
        car = factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        factory = CarFactory()
        car = factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        warning_light_is_on = False

        factory = CarFactory()
        car = factory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)
        warning_light_is_on = False

        factory = CarFactory()
        car = factory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        warning_light_is_on = True

        factory = CarFactory()
        car = factory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date
        warning_light_is_on = False

        factory = CarFactory()
        car = factory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        factory = CarFactory()
        car = factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        factory = CarFactory()
        car = factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date
        current_mileage = 60001
        last_service_mileage = 0

        factory = CarFactory()
        car = factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date
        current_mileage = 60000
        last_service_mileage = 0

        factory = CarFactory()
        car = factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        factory = CarFactory()
        car = factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        factory = CarFactory()
        car = factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date
        current_mileage = 60001
        last_service_mileage = 0

        factory = CarFactory()
        car = factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        today = last_service_date
        current_mileage = 30000
        last_service_mileage = 0

        factory = CarFactory()
        car = factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
