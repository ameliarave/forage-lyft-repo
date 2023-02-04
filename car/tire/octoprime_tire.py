from car.tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_array):
        self.__tire_array = tire_array
    
    def needs_service():
        sum = 0
        for x in self.__tire_array:
            sum += x

        if sum >= 3:
            return True
        return False