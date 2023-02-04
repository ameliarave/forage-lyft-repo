from abc import ABC
#from serviceable import Serviceable
#from car.car import Car
from car.battery.battery import Battery
from datetime import datetime

class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.__last_service_date = last_service_date
        self.__current_date = current_date
    
    def needs_service(self):
        service_threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False