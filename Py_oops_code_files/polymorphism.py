# Exercise 16: Polymorphism with Dog & Cat speak()

class Animal():
    def __init__(self, name):
        self.name = name

    def speak():
        print('Animal Speaking')

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)

    def speak(self):
        print('Bow Bow')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Meow Meow')


dog1 = Dog('Jimmy')
cat1 = Cat('Clark')
dog1.speak()
cat1.speak()