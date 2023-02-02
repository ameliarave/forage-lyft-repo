from abc import ABC
#from serviceable import Serviceable
#from car.car import Car
from car.engine.engine import Engine

class WilloughbyEngine(Engine, ABC):
    def __init__(self, last_service_mileage, current_mileage):
        super().__init__()
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    def needs_service(self):
        print("Checking if WilloughbyEngine needs service")
        return self.__current_mileage - self.__last_service_mileage > 60000
