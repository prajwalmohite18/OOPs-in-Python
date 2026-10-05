# Exercise 2: Vehicle Class with Instance Attributes
class Vehicle:
    # Constructor
    def __init__(self,max_speed, mileage):
        # Instance Attributes
        self.max_speed = max_speed
        self.mileage = mileage

vehicle1 = Vehicle(100,60)

print(f'Max Speed: {vehicle1.max_speed}\nMileage: {vehicle1.mileage}')

