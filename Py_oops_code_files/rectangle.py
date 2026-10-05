# Exercise 3: Rectangle Class with Area & Perimeter

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return (self.length*self.width)
    
    def perimeter(self):
        return 2*(self.length+self.width)

A4sheet = Rectangle(21, 29.7)

print(A4sheet)
print(f'A4 Sheet Length: {A4sheet.length}, A4 Sheet Width: {A4sheet.width}')
print(f'A4 Sheet Perimeter: {A4sheet.perimeter()}, A4 Sheet Area: {A4sheet.area()}')