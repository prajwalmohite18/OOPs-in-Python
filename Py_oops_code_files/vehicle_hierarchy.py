# Exercise 21: Vehicle Class Hierarchy with Bike, Truck & Bus

class Vechicle():

    def __init__(self,speed):
        self.max_speed = speed

    def describe(self):
            print(f'{self.__class__.__name__} Max Speed: {self.max_speed} km/h')

class Bike(Vechicle):

    def __init__(self, speed):
        super().__init__(speed)

    
class Truck(Vechicle):

    def __init__(self, speed):
        super().__init__(speed)

class Bus(Vechicle):
    
    def __init__(self, speed):
        super().__init__(speed)        

b1 = Bike(150)
b1.describe()

t1 = Truck(80)
t1.describe()

bus1 = Bus(100)
bus1.describe()
