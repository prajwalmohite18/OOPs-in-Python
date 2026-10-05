# Exercise 29: Zoo Class that Feeds All Animals

# Base Class
class Animal:
    def __init__(self):
        pass

    def eat(self):
        print('Animal eats')

# subclasses
class Dog(Animal):
    def __init__(self):
        pass

    def eat(self):
        print("Dog eats Pedigeree")

class Cat(Animal):
    def __init__(self):
        pass

    def eat(self):
        print("Cat eats fish")

class Lion(Animal):
    def __init__(self):
        pass

    def eat(self):
        print('Lion eats meat')


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def feed_all(self):
        for animal in self.animals:
            animal.eat()
            
    def add_to_zoo(self, animal):
        self.animals.append(animal)

Mysuru_Zoo = Zoo('Mysuru Zoo')

Mysuru_Zoo.add_to_zoo(Cat())
Mysuru_Zoo.add_to_zoo(Dog())
Mysuru_Zoo.add_to_zoo(Lion())

Mysuru_Zoo.feed_all()