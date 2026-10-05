# Exercise 9: Temperature Class with Unit Converters

class Temperature():

    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return ((9/5)*self.celsius + 32)

    def to_kelvin(self):
        return self.celsius+273.15

day_temp = Temperature(100)
print('Celsius:', day_temp.celsius)
print('Fahrenheit :', day_temp.to_fahrenheit())
print('Kelvin :', day_temp.to_kelvin())