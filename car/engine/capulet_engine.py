from car.engine.engine import Engine


class CapuletEngine(Engine): # serviced every 30,000 miles
    def __init__(self, current_mileage, last_service_mileage):
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.__current_mileage - self.__last_service_mileage > 30000
