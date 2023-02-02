from abc import ABC, abstractmethod
#from serviceable import Serviceable
#from car.car import Car

class Engine(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def needs_service():
        pass
