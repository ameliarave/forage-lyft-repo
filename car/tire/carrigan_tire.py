from car.tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_array):
        self.__tire_array = tire_array
    
    def needs_service():
        count = 0
        for x in self.__tire_array:
            if x >= 0.9:
                return True
        return False
        