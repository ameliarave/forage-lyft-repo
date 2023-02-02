from abc import ABC
#from serviceable import Serviceable
#from car.car import Car
from car.engine.engine import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_is_on):
        super().__init__()
        self.__warning_light_is_on = warning_light_is_on

    def needs_service(self):
        print("Checking if SternmanEngine needs service")
        if self.__warning_light_is_on:
            return True
        else:
            return False
