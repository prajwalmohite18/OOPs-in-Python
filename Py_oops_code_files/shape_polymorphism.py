# Exercise 18: Shape Subclasses with Custom area() Methods

class Shape():
    def __init__(self, side):
        self.side = side

    def area():
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius)

    # polymorphism
    def area(self):
        pi = 22/7
        ar = pi*self.radius**2
        print(f'Aree of Circle of radius {self.radius} is {ar}')
        return ar

class Square(Shape):
    def __init__(self, side):
        super().__init__(side)

    def area(self):
        ar = self.side**2
        print(f'Area of Sqaure of side {self.side} is {ar}')
        return ar

class Triangle(Shape):
    def __init__(self, sideA, sideB, sideC):
        self.sideA = sideA
        super().__init__(sideA)
        self.sideB = sideB
        self.sideC = sideC

    def area(self):
        s = (self.sideA + self.sideB + self.sideC)/2
        ar = ((s * (s -self.sideA) * (s-self.sideB) * (s-self.sideC))**0.5)
        print(f'Area of triangle of sides {self.sideA}, {self.sideB} and {self.sideC} is {ar}')
        return ar

c1 = Circle(50)
s1 = Square(25)
t1 = Triangle(3,4,5)
c1.area()
s1.area()
t1.area()

# shapes = [c1, s1, t1]

# for shape in  shapes:
#     print(f'{type(shape).__name__} area : {shape.area()}')