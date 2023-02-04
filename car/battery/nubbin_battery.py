from car.battery.battery import Battery
from datetime import datetime

class NubbinBattery(Battery):    # once every 4 years
    def __init__(self, current_date, last_service_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date
    
    def needs_service(self):
        service_threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 4)
        if service_threshold_date < self.__current_date:
            return True
        else:
            return False
