# Exercise 24: Vector Addition Using add Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, vector_objs):
        return Vector(self.x + vector_objs.x, self.y + vector_objs.y)


vector_1 = Vector(1,3)
vector_2 = Vector(1,4)

new_vec = vector_1+vector_2
print(f'Vector({new_vec.x}, {new_vec.y})')

