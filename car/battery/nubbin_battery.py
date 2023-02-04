from abc import ABC
from car.battery.battery import Battery
from datetime import datetime

class NubbinBattery(Battery, ABC):    # once every 4 years
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.__last_service_date = last_service_date
        self.__current_date = current_date
    
    def needs_service(self):
        service_threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 4)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
