# Exercise 12: Shared Class Attribute Across Instances 

class Vechicle():
    # class attribute
    color = 'White'
    
    def __init__(self, name, speed):
        # instance attributes
        self.name = name
        self.speed = speed

car1 = Vechicle('Tesla', 150)
car2 = Vechicle('BMW', 300)

print(f'{car1.name} - Color: {car1.color}, Speed: {car1.speed}')
print(f'{car2.name} - Color: {car2.color}, Speed: {car2.speed}')

Vechicle.color = 'Red' 
# class attribute value has been changed that affect all objects of Vechicle class.

print(f'{car1.name} - Color: {car1.color}, Speed: {car1.speed}')
print(f'{car2.name} - Color: {car2.color}, Speed: {car2.speed}')