# Exercise 14: Override Parent Method Using super()

class Vehicle():
    def __init__(self, name):
        self.name = name
        
    def seating_capacity(self,capacity):
        print(f'{self.name} seating capacity is  {capacity}')

class Bus(Vehicle):

    def seating_capacity(self):
        super().seating_capacity(50)

bus1 = Bus('Tata')
print('Bus Name:',bus1.name)
bus1.seating_capacity()