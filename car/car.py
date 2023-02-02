from abc import ABC, abstractmethod
from serviceable import Serviceable


class Car(Serviceable, ABC):
    def __init__(self, engine, battery):
        super().__init__()
        self.__engine = engine
        self.__battery = battery

    def needs_service(self):
        if self.__engine.needs_service() or self.__battery.needs_service():
            return True
        else:
            return False
