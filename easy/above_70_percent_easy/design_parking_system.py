"""
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small,
with a fixed number of slots for each size.

Implement the ParkingSystem class:

    * ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class.
     The number of slots for each parking space are given as part of the constructor.
    * bool addCar(int carType) Checks whether there is a parking space of carType for the car
     that wants to get into the parking lot. carType can be of three kinds: big, medium, or small,
     which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of
     its carType. If there is no space available, return false, else park the car in that size space and return true.
"""


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking_lot = {1: big, 2: medium, 3: small}

    def add_car(self, car_type: int) -> bool:
        if car_type not in self.parking_lot or self.parking_lot[car_type] == 0:
            return False
        self.parking_lot[car_type] -= 1
        return True


if __name__ == '__main__':
    obj = ParkingSystem(2, 1, 0)
    print(obj.add_car(1))
    print(obj.add_car(1))

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
