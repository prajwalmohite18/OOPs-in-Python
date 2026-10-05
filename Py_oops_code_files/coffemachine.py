# Exercise 11: Coffee Machine with Multi-Resource Tracking

class CoffeMachine():
    def __init__(self,  water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk 

    def make_latte(self):
        if self.water >= 200 and self.coffee >= 20 and self.milk >= 150:
            self.water -= 200
            self.coffee -= 20
            self.milk -= 150
            print(f'Latte made! Remaining - Water:{self.water}ml, Coffee: {self.coffee}ml, Milk:{self.milk}')
        else:
            print('Not enough resources to make a latte.')

c1 = CoffeMachine(500, 100, 300)
c1.make_latte()
c1.make_latte()
c1.make_latte()