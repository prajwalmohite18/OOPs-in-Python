# Exercise 13: Bus Subclass Inheriting from Vehicle

class Vechicle():

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f'Vehicle Name:{self.name} Max Speed: {self.max_speed}km/h')

# subclass
# Bus subclass inherites all the parent Vechile class attributes and methods.
class Bus(Vechicle):
    pass

bus1 = Bus('Tata',140)

# Parent class attributes
print(bus1.name, bus1.max_speed)

# Parent class method
bus1.display() 