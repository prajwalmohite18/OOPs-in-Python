# Exercise 23: Type Checking with isinstance() & issubclass()

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

c = Cat('Coko')
d = Dog('Jimmy')
a = Animal('Tiger')

print(f'Is d is instace of Dog? {isinstance(d,Dog)}')
print(f'Is c is instance of Cat? {isinstance(c, Cat)}')
print(f'Is a is instance of Animal {isinstance(a, Animal)}')
print(f'Is a is instance of Dog? {isinstance(a, Dog)}')
print(f'Is d is instance of Animal {isinstance(d, Animal)}')
print(f'Is Dog is subclass of Animal?{issubclass(Dog, Animal)}')
print(f'Is Cat is subclass of Animal?{issubclass(Cat, Animal)}')
print(f'Is Animal is subclass of Cat?{issubclass(Animal, Cat)}')

