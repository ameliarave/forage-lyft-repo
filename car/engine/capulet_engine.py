from abc import ABC
#from serviceable import Serviceable
#from car.car import Car
from car.engine.engine import Engine


class CapuletEngine(Engine, ABC): # serviced every 30,000 miles
    def __init__(self, last_service_mileage, current_mileage):
        super().__init__()
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    def needs_service(self):
        print("Checking if CapuletEngine needs service")
        return self.__current_mileage - self.__last_service_mileage > 30000
