from car.car import Car
from car.battery.nubbin_battery import NubbinBattery
from car.battery.spindler_battery import SpindlerBattery
from car.engine.capulet_engine import CapuletEngine
from car.engine.sternman_engine import SternmanEngine
from car.engine.willoughby_engine import WilloughbyEngine
from car.tire.carrigan_tire import CarriganTire
from car.tire.octoprime_tire import OctoprimeTire

class CarFactory():
    def __init__(self):
        pass

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_array):  # Capulet / Spindler
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tire_array)        
        return Car(engine, battery, tires)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_array): # Willoughby / Spindler
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTire(tire_array)
        return Car(engine, battery, tires)

    def create_palindrome(self, current_date, last_service_date, warning_light_is_on, tire_array): # Sternman / Spindler
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTire(tire_array)
        return Car(engine, battery, tires)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_array): # Willoughby / Nubbin
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTire(tire_array)
        return Car(engine, battery, tires)
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_array): # Capulet / Nubbin
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTire(tire_array)
        return Car(engine, battery, tires)
