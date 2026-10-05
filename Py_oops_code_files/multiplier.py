# Exercise 27: Callable Object Class Using call

class Multiplier:

    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return self.factor*value
    
triple = Multiplier(3)
double = Multiplier(2)
print(triple(10))
print(double(40))