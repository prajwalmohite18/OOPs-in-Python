# Exercise 4: Student Class with Average Grade
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        avg = sum(self.marks)/len(self.marks)
        return avg

s1 = Student('Ram', [10,20,30])
print('Name:',s1.name,'Average Marks:', s1.average())
