# Exercise 14: Override Parent Method Using super()

class Factory():
    a = 445

    print('Intialized')
    
    @classmethod
    def greet():
        return (f'Good Morning')

a  = Factory()
# print(Factory.a)
print(a.greet())