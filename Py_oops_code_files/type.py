# Exercise 22: Identify Object’s Class Using type()

class Engineer:
    pass

class Doctor:
    pass

class Teacher:
    pass

Ram = Engineer()
Raman = Doctor()
Vishnu = Teacher()

print('Ram:',type(Ram).__name__)
print('Raman:',type(Raman).__name__)
print('Vishnu:',type(Vishnu).__name__)