# Exercise 15: Add Maintenance Fee in Child Class via super()

class Vechicle():
    
    def __init__(self, base_fare):
        self.base_fare = base_fare


class Taxi(Vechicle):
    
    def __init__(self,base_fare):
        super().__init__(base_fare)
        self.maintainence_fee = 0.1 * base_fare

    def total_fare(self):
        return self.base_fare + self.maintainence_fee
    
taxi1=Taxi(base_fare = 500)
print('Total Fare:',taxi1.total_fare())