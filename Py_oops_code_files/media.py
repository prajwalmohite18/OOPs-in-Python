# Exercise 19: Media Subclasses with Type-Specific Attributes

class Media():

    def __init__(self, title, price):
        self.title = title
        self.price = price
        
class Book(Media):

    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author

    def describe(self):
        print(f'Book: {self.title} by {self.author} - {self.price}rs')


class DVD(Media):
    def __init__(self, title, price, duartion):
        super().__init__(title, price)
        self.duration = duartion

    def describe(self):
        print(f'DVD: {self.title}, {self.duration} - {self.price}rs')

class Magazine(Media):
    def __init__(self, title, price, mag_type):
        super().__init__(title, price)
        self.mag_type = mag_type

    def describe(self):
        print(f'Magzine: {self.title} ({self.mag_type}) - {self.price}rs')

b1 = Book("Clean Code", 499, "Robert C. Martin")
m1 = Magazine("Wired", 150, "Monthly")
d1 = DVD("Inception", 299, 148)

b1.describe()
m1.describe()
d1.describe()