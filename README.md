# Python Object-Oriented Programming(OOP) Exercise
**[Exercise 1: Define an Empty Vehicle Class](/Py_oops_code_files/emptyclass.py)**
**Problem Statement:** Write a Python program to create a class named `Vehicle` that has no variables or methods defined inside it.
```py []
class Vehicle:
    # Empty Class
    pass

print(Vehicle) 
print(type(Vehicle))

# OUTPUT
<class '__main__.Vehicle'>
<class 'type'>
```
**[Exercise 2: Vehicle Class with Instance Attributes](Py_oops_code_files/vehicle.py)**
**Problem Statement:** Write a Python program to create a `Vehicle` class with two instance attributes: `max_speed` and `mileage`. Create an object of the class and print both attributes.

```py []
class Vehicle:
    # Constructor
    def __init__(self,max_speed, mileage):
        # Instance Attributes
        self.max_speed = max_speed
        self.mileage = mileage

vehicle1 = Vehicle(100,60)

print(f'Max Speed: {vehicle1.max_speed}\nMileage: {vehicle1.mileage}')

# OUTPUT
Max Speed: 100
Mileage: 60
```

**[Exercise 3: Rectangle Class with Area & Perimeter](Py_oops_code_files/rectangle.py)**
**Problem Statment:** Write a Python program to create a `Rectangle` class with `length` and `width` as instance attributes, and two methods: `area()` that returns the area and `perimeter()` that returns the perimeter.

```py []
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

# OUTPUT
<__main__.Rectangle object at 0x00000245F8460F80>
A4 Sheet Length: 21, A4 Sheet Width: 29.7
A4 Sheet Perimeter: 101.4, A4 Sheet Area: 623.6999999999999
```
**[Exercise 4: Student Class with Average Grade](Py_oops_code_files/student.py)**
**Problem Statement:** Write a Python program to create a `Student` class that stores a student’s `name` and a list of `marks`. Add a method `average()` that calculates and returns the average of all marks.
```py []
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        avg = sum(self.marks)/len(self.marks)
        return avg

s1 = Student('Ram', [10,20,30])
print('Name:',s1.name,'Average Marks:', s1.average())

# OUTPUT
Name: Ram Average Marks: 20.0
```
**[Exercise 5: Product Class with Stock Value Calculator](Py_oops_code_files/product.py)**
**Problem Statement:** Write a Python program to create a `Product` class with three instance attributes: `name`, `price`, and `quantity`. Add a method `total_value()` that returns the total stock value by multiplying price by quantity.
```py []
class Product:
    def __init__(self, name, price, quantity):
        # Instance Attributes
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return (self.quantity * self.price)

laptop = Product('Laptop', 50000, 10)

print('Product Name:', laptop.name, 'Product Price:',laptop.price, 'No of Products', laptop.quantity)
print('Total stock value of', laptop.name, 'is', laptop.total_value())

# OUTPUT
Product Name: Laptop Product Price: 50000 No of Products 10
Total stock value of Laptop is 500000
```


**[Exercise 6: Bank Account with Deposit & Overdraw Protection ](Py_oops_code_files/bankAccount.py)**
**Problem Statement:** Write a Python program to create a `BankAccount` class with a `balance` attribute and two methods: `deposit(amount)` that adds funds to the balance, and `withdraw(amount)` that deducts funds but prevents the balance from going below zero.

```py []
class BankAccount():
    def __init__(self, balance):
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        print('Balance after deposit:', self.balance)

    def withdrawal(self, amount):
        if amount > self.balance:
            print('Insufficient funds. Current balance:', self.balance)
        else:
            self.balance -= amount
            print('Balance after withdrawal:', self.balance)


b_acc1 = BankAccount(5000)
print('Bank Account Intial Balance:', b_acc1.balance)
b_acc1.deposit(1000)
b_acc1.withdrawal(400)
b_acc1.withdrawal(100000)

# OUTPUT
Bank Account Intial Balance: 5000
Balance after deposit: 6000
Balance after withdrawal: 5600
Insufficient funds. Current balance: 5600
```

**[Exercise 7: Light Class with On/Off State Toggle](Py_oops_code_files/light.py)**
**Problem Statement:** Write a Python program to create a `Light` class with three methods: `turn_on()` that switches the light on, `turn_off()` that switches it off, and `status()` that reports whether the light is currently on or off.
```py []
class Light():

    def __init__(self):
        self.is_on = False
   
    def turn_on(self):
        self.is_on = True
        print('Light is ON')

    def turn_off(self):
        self.is_on = False
        print('Light is OFF')

    def status(self):
        state = 'ON' if self.is_on else 'OFF'
        print('Current Status:', state)

lamp1 = Light()
lamp1.status()
lamp1.turn_on()
lamp1.status()
lamp1.turn_off()
lamp1.status()

# OUTPUT
Current Status: OFF
Light is ON
Current Status: ON
Light is OFF
Current Status: OFF
```

**[Exercise 8: User Class with Password Validation](Py_oops_code_files/passwordValidation.py)**
**Problem Statement:** Write a Python program to create a `User` class that stores a `username` and a `password`. Add a `check_password(input_password)` method that returns True if the input matches the stored password, and False otherwise.

```py []
class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password
        
user1 = User('shyam', 'shyam123')
print(user1.check_password('shyam123'))
print(user1.check_password('shyam1234'))
 
# OUTPUT
True
False
```
**[Exercise 9: Temperature Class with Unit Converters](Py_oops_code_files/temperature.py)**
**Problem Statement:** Write a Python program to create a `Temperature` class that stores a temperature in Celsius. Add two methods: `to_fahrenheit()` that converts and returns the value in Fahrenheit, and `to_kelvin()` that converts and returns the value in Kelvin.


``` py []
class Temperature():

    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return ((9/5)*self.celsius + 32)

    def to_kelvin(self):
        return self.celsius+273.15

day_temp = Temperature(100)
print('Celsius:', day_temp.celsius)
print('Fahrenheit :', day_temp.to_fahrenheit())
print('Kelvin :', day_temp.to_kelvin())

# OUTPUT
Celsius: 100
Fahrenheit : 212.0
Kelvin : 373.15 
```
**[Exercise 10: Notebook Class with Add & Display Notes](Py_oops_code_files/notebook.py)**
**Problem Statement:** Write a Python program to create a `Notebook` class that maintains an internal list of notes. Add an `add_note(note)` method that appends a new note to the list, and a `show_notes()` method that prints all stored notes.
```py []
class Notebook():

    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def show_notes(self):
        for i, note in enumerate(self.notes):
            print(i+1,note)

nb1 = Notebook()
nb1.add_note('Buy Groceries')
nb1.add_note('Read a book')
nb1.add_note('Wash Clothes')
nb1.add_note('Meditate')
nb1.show_notes()

# OUTPUT
1 Buy Groceries
2 Read a book
3 Wash Clothes
4 Meditate
```
**[Exercise 11: Coffee Machine with Multi-Resource Tracking](Py_oops_code_files/coffemachine.py)**
**Problem Statement:** Write a Python program to create a `CoffeeMachine` class that tracks three resource attributes: `water`, `coffee`, and `milk` (in ml/g). Add a `make_latte`() method that checks whether sufficient resources are available, deducts them if so, and prints an appropriate message in either case.
```py []
class CoffeMachine():
    def __init__(self,  water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk 

    def make_latte(self):
        if self.water >= 200 and self.coffee >= 20 and self.milk >= 150:
            self.water -= 200
            self.coffee -= 20
            self.milk -= 150
            print(f'Latte made! Remaining - Water:{self.water}ml, Coffee: {self.coffee}ml, Milk:{self.milk}')
        else:
            print('Not enough resources to make a latte.')

c1 = CoffeMachine(500, 100, 300)
c1.make_latte()
c1.make_latte()
c1.make_latte()

# OUTPUT
Latte made! Remaining - Water:300ml, Coffee: 80ml, Milk:150
Latte made! Remaining - Water:100ml, Coffee: 60ml, Milk:0
Not enough resources to make a latte.
```

**[Exercise 12: Shared Class Attribute Across Instances](Py_oops_code_files/shared_class_attributes.py)**
**Problem Statement:** Write a Python program to create a `Vehicle` class with a class attribute `color = "White"` that is shared by all instances. Create two vehicle objects and demonstrate that both share the same default color, then show that changing the class attribute updates all instances that have not overridden it

```py []
class Vechicle():
    # class attribute
    color = 'White'
    
    def __init__(self, name, speed):
        # instance attributes
        self.name = name
        self.speed = speed

car1 = Vechicle('Tesla', 150)
car2 = Vechicle('BMW', 300)

print(f'{car1.name} - Color: {car1.color}, Speed: {car1.speed}')
print(f'{car2.name} - Color: {car2.color}, Speed: {car2.speed}')

Vechicle.color = 'Red' 
# class attribute value has been changed that affect all objects of Vechicle class.

print(f'{car1.name} - Color: {car1.color}, Speed: {car1.speed}')
print(f'{car2.name} - Color: {car2.color}, Speed: {car2.speed}')

# OUTPUT
Tesla - Color: White, Speed: 150
BMW - Color: White, Speed: 300
Tesla - Color: Red, Speed: 150
BMW - Color: Red, Speed: 300
```

**[Exercise 13: Bus Subclass Inheriting from Vehicle](Py_oops_code_files/bus_subclass.py)**
**Problem Statement:** Write a Python program to create a `Vehicle` parent class with name and `max_speed` attributes and a `display()` method. Then create a `Bus` child class that inherits everything from `Vehicle` without adding anything new, and confirm that an instance of `Bus` can access the parent’s method.
```py []
class Vechicle():

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f'Vehicle Name:{self.name} Max Speed: {self.max_speed}km/h')

# subclass
# Bus subclass inherites all the parent Vechile class attributes and methods.
class Bus(Vechicle):
    pass

bus1 = Bus('Tata',140)

# Parent class attributes
print(bus1.name, bus1.max_speed)

# Parent class method
bus1.display()

# OUTPUT
Tata 140
Vehicle Name:Tata Max Speed: 140km/h
```
**[Exercise 14: Override Parent Method Using super()](Py_oops_code_files/override.py)**
**Problem Statement:** Write a Python program where a `Vehicle` parent class has a `seating_capacity()` method that accepts a capacity argument. Create a `Bus` child class that overrides this method to provide a default seating capacity of `50`, using `super()` to call the parent’s version internally.
```py []
class Vehicle():
    def __init__(self, name):
        self.name = name
        
    def seating_capacity(self,capacity):
        print(f'{self.name} seating capacity is  {capacity}')

class Bus(Vehicle):

    def seating_capacity(self):
        super().seating_capacity(50)

bus1 = Bus('Tata')
print('Bus Name:',bus1.name)
bus1.seating_capacity()

# OUTPUT
Bus Name: Tata
Tata seating capacity is  50
```

**[Exercise 15: Add Maintenance Fee in Child Class via super()](Py_oops_code_files/taxi.py)**
**Problem Statement:** Write a Python program that creates a `Vehicle` parent class with a base fare, then extends a `Taxi` child class that adds a 10% maintenance fee on top of the base fare using `super()`.
```py []
class Vechicle():
    
    def __init__(self, base_fare):
        self.base_fare = base_fare


class Taxi(Vechicle):
    
    def __init__(self,base_fare):
        super().__init__(base_fare)
        self.maintainence_fee = 0.1 * base_fare

    def total_fare(self):
        return self.base_fare + self.maintainence_fee

taxi1=Taxi(base_fare = 500)
print('Total Fare:',taxi1.total_fare())

# OUTPUT
Total Fare: 550.0
```

**[Exercise 16: Polymorphism with Dog & Cat speak()](Py_oops_code_files/polymorphism.py)**
**Problem Statement:** Write a Python program that defines an `Animal` base class with a `speak()` method, then overrides it in `Dog` and `Cat` subclasses to return their respective sounds.
```py []
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

# OUTPUT
Bow Bow
Meow Meow
```

**[Exercise 17: Full-Time vs Part-Time Employee Pay Logic](Py_oops_code_files/employee_inheritence.py)**
**Problem Statement:** Write a Python program that defines an `Employee` base class, then creates `FullTimeEmployee` and `PartTimeEmployee` subclasses, each implementing different pay calculation logic.
``` py []
class Employee():
    def __init__(self,name):
        self.name = name

    def calculate_pay(self):
        return 0

class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        self.monthly_salary = self.annual_salary/12
        print(f'{self.name} monthly salary is {self.monthly_salary}')
         
        
class PartTimeEmployee(Employee):
    def __init__(self, name, hour_salary, working_hours):
        super().__init__(name)
        self.hour_salary = hour_salary
        self.working_hours = working_hours

    def calculate_pay(self):
        self.monthly_salary = self.hour_salary * self.working_hours
        print(f'{self.name} monthly salary is {self.monthly_salary}')

ft_emp1 = FullTimeEmployee('Alice', 500000)
pt_emp1= PartTimeEmployee('Bob', 500, 20)
ft_emp1.calculate_pay()
pt_emp1.calculate_pay()

# OUTPUT
Alice monthly salary is 41666.666666666664
Bob monthly salary is 10000
```

**[Exercise 18: Shape Subclasses with Custom area() Methods](Py_oops_code_files/shape_polymorphism.py)**
**Problem Statement:** Write a Python program that defines a `Shape` base class with an `area()` method, then implements it in `Circle`, `Square`, and `Triangle` subclasses using the appropriate geometric formulas.
```py []
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
```

**[Exercise 19: Media Subclasses with Type-Specific Attributes](Py_oops_code_files/media.py)**
**Problem Statement:** Write a Python program that defines a `Media` base class, then creates `Book`, `Magazine`, and `DVD` subclasses, each with type-specific attributes and a `describe()` method.

```py []
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

# OUTPUT
Book: Clean Code by Robert C. Martin - 499rs
Magzine: Wired (Monthly) - 150rs
DVD: Inception, 148 - 299rs
```
**[Exercise 20: Discounted Order Subclass with 10% Off](Py_oops_code_files/order.py)**
**Problem Statement:** Write a Python program that creates an `Order` class with a total amount, then creates a `DiscountedOrder` subclass that applies a 10% discount to the total.
```py []
class Order:
    def __init__(self, order_id,total_amount):
        self.order_id = order_id
        self.total_amount = total_amount

    def get_total(self):
        return self.total_amount
    
class DiscountedOrder(Order):
    def __init__(self, order_id, total_amount):
        super().__init__(order_id, total_amount)
        self.discounted_amount = total_amount - 0.1*total_amount

    def get_total(self):
        return self.discounted_amount

order1 = DiscountedOrder('ord1001', 2000)
print('Order ID:',order1.order_id)
print('Original Total:',order1.total_amount)
print('Discounted Total:', order1.get_total())

# OUTPUT
Order ID: ord1001
Original Total: 2000
Discounted Total: 1800.0
```

**[Exercise 21: Vehicle Class Hierarchy with Bike, Truck & Bus](Py_oops_code_files/vehicle_hierarchy.py)**
**Problem Statement:** Write a Python program that defines a `Vehicle` base class and creates `Bike`, `Truck`, and `Bus` subclasses, each defining a unique `max_speed` attribute and a `describe()` method.
```py []
class Vechicle():

    def __init__(self,speed):
        self.max_speed = speed

    def describe(self):
            print(f'{self.__class__.__name__} Max Speed: {self.max_speed} km/h')

class Bike(Vechicle):

    def __init__(self, speed):
        super().__init__(speed)

    
class Truck(Vechicle):

    def __init__(self, speed):
        super().__init__(speed)

class Bus(Vechicle):
    
    def __init__(self, speed):
        super().__init__(speed)        

b1 = Bike(150)
b1.describe()

t1 = Truck(80)
t1.describe()

bus1 = Bus(100)
bus1.describe()

# OUTPUT
Bike Max Speed: 150 km/h
Truck Max Speed: 80 km/h
Bus Max Speed: 100 km/h
```

**[Exercise 22: Identify Object’s Class Using type()](Py_oops_code_files/type.py)**
**Problem Statement:** Write a Python program that creates objects from multiple classes and uses the built-in `type()` function to identify which class each object belongs to.

```py []
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

# OUTPUT
Ram: Engineer
Raman: Doctor
Vishnu: Teacher
```

**[Exercise 23: Type Checking with isinstance() & issubclass()](Py_oops_code_files/type_check.py)**
**Problem Statement:** Write a Python program that uses `isinstance()` to check whether an object is an instance of a given class, and `issubclass()` to check whether one class is a subclass of another.
```py []
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

# OUTPUT
Is d is instace of Dog? True
Is c is instance of Cat? True
Is a is instance of Animal True
Is a is instance of Dog? False
Is d is instance of Animal True
Is Dog is subclass of Animal?True
Is Cat is subclass of Animal?True
Is Animal is subclass of Cat?False
```

**[Exercise 24: Vector Addition Using add Overloading](Py_oops_code_files/operator_overloading.py)**
**Problem Statement:** Write a Python program that creates a `Vector` class representing a 2D vector, and implements the `__add__` dunder method so that two `Vector` objects can be added using the `+` operator.
```py []
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, vector_objs):
        return Vector(self.x + vector_objs.x, self.y + vector_objs.y)


vector_1 = Vector(1,3)
vector_2 = Vector(1,4)

new_vec = vector_1+vector_2
print(f'Vector({new_vec.x},{new_vec.y})')

# OUTPUT
Vector(2,7)   
```
**[Exercise 25: Cart Length Using len Overloading](Py_oops_code_files/len_func_imp.py)**
**Problem Statement:** Write a Python program that creates a `Cart` class that stores a list of items, and implements `__len__` so that calling `len(cart)` returns the number of items currently in the cart.
```py []
# Exercise 25: Cart Length Using len Overloading

class Cart:

    def __init__(self, item):
        self.items = [item]

    def add_to_cart(self,item):
        self.items.append(item)
        return item
    
    def __len__(cart_obj):
        return len(cart_obj.items)

my_cart = Cart('Cricket Bat')
print('Items in My Cart:',my_cart.items)
print('No of items in My Cart:',len(my_cart))

print()

my_cart.add_to_cart('Dairy')
my_cart.add_to_cart('Friuts')
my_cart.add_to_cart('Vegetables')
print('Items in My Cart:',my_cart.items)
print('No of items in My Cart:',len(my_cart))

# OUTPUT
Items in My Cart: ['Cricket Bat']
No of items in My Cart: 1

Items in My Cart: ['Cricket Bat', 'Dairy', 'Friuts', 'Vegetables']
No of items in My Cart: 4
```

**[Exercise 26: Private Balance with Property Getter & Setter](Py_oops_code_files/getter_setter.py)**
**Problem Statement:** Write a Python program that creates a `BankAccount` class where the balance is stored as a private attribute `__balance`, and exposed safely through a `@property` getter and a setter that validates the value before updating it.
```py []
class BankAccount:

    def __init__(self, intial_deposit):
        self.__balance = intial_deposit

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance<0:
            print('Invaild amount')
        else:
            self.__balance = balance

    def deposit(self, amount):
        if amount<0:
            print('Invalid amount. Must be non-negative')
        else:
            self.balance += amount

    def withdrawl(self, amount):
        self.balance -= amount

acc_1 = BankAccount(32413)
print(acc_1.balance)
acc_1.deposit(1000)
print(acc_1.balance)
acc_1.withdrawl(acc_1.balance+1)

# OUTPUT
32413
33413
Invaild amount
```
**[Exercise 27: Callable Object Class Using call](Py_oops_code_files/multiplier.py)**
**Problem Statement:** Write a Python program that creates a `Multiplier` class which stores a factor, and implements `__call__` so that an instance of the class can be invoked directly like a function to multiply a given number by that factor.

```py []
class Multiplier:

    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return self.factor*value
    
triple = Multiplier(3)
double = Multiplier(2)
print(triple(10))
print(double(40))

# OUTPUT
30
80
```

**[Exercise 28: Flight Class with Passenger Capacity Check](Py_oops_code_files/book_flight.py)**
**Problem Statement:** Write a Python program that creates a Passenger class and a `Flight` class. The `Flight` class should manage a list of `Passenger` objects and block further bookings when the seat capacity is reached.
```py []
class Passenger:

    def __init__(self, name):
        self.name = name

class Flight():

    def __init__(self, flight_code, seat_capacity):
        self.flight_code = flight_code
        self.seat_capacity = seat_capacity
        self.booked_passengers = []

    def book_flight(self, Passenger):
        if len(self.booked_passengers) < self.seat_capacity:
            self.booked_passengers.append('Passenger.name')
            print(f'{Passenger.name} is booked on Flight {self.flight_code} sucessfully.')
        else:
            print(f'Sorry, Flight {self.flight_code} is fully booked.')


flight1 = Flight('AI101', 2)
flight1.book_flight(Passenger('Kalam'))
flight1.book_flight(Passenger('Tiru'))
flight1.book_flight(Passenger('Raj'))

# OUTPUT
Kalam is booked on Flight AI101 sucessfully.
Tiru is booked on Flight AI101 sucessfully.
Sorry, Flight AI101 is fully booked.
```

**[Exercise 29: Zoo Class that Feeds All Animals](Py_oops_code_files/zoo.py)**
**Problem Statement:** Write a Python program that defines an `Animal` base class with an `eat()` method, creates a few subclasses with their own `eat()` implementations, and builds a `Zoo` class that holds a list of animals and calls `eat()` on all of them via a `feed_all()` method.

```py []
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

# OUTPUT
Cat eats fish
Dog eats Pedigeree
Lion eats meat
```

**[Exercise 30: Character Class with Auto Level-Up Logic](Py_oops_code_files/Character.py)**
**Problem Statement:** Write a Python program that creates a `Character` class with `health`, `exp`, and `level` attributes. The character should automatically level up and reset `exp` whenever accumulated experience reaches or exceeds 100.
```py []
class Character:
    def __init__(self,name, health):
        self.name = name
        self.health = health
        self.exp = 0
        self.level = 1

    def gain_exp(self, amount):
        if amount > 0 and isinstance(amount, (int, float)):
            if self.exp + amount < 100:
                self.exp += amount 
                print(f'{self.name} gained {amount} exp. (Total:{self.exp})')

            else:           
                level_up = (self.exp+amount)// 100 # logic to increment to many level_ups
                rem_exp = (self.exp+amount)%100 # remaining exp, after self.exp = 100 
                self.level += level_up
                self.exp = rem_exp
                print(f'{self.name} gained {amount} exp.Level Up! Now Level {self.level}. (Remaining exp: {rem_exp})')
        else:
            print('Enter a valid gain exp')

ch_Cj = Character('Cj', 100)
ch_Micheal = Character('Micheal', 100)

ch_Cj.gain_exp(60)
ch_Cj.gain_exp(60)

ch_Micheal.gain_exp(50)
ch_Micheal.gain_exp(460)

# OUTPUT
Cj gained 60 exp. (Total:60)
Cj gained 60 exp.Level Up! Now Level 2. (Remaining exp: 20)
Micheal gained 50 exp. (Total:50)
Micheal gained 460 exp.Level Up! Now Level 6. (Remaining exp: 10)
```

**[Exercise 31: Playlist Class with Add, Remove & Shuffle](Py_oops_code_files/songs.py)**
**Problem Statement:** Write a Python program that defines a `Song` class and a `Playlist` class. The `Playlist` should support adding songs, removing songs by title, and shuffling the order of the playlist randomly.

```py []
import random
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            print(f'{song.title} added to Playlist.')
        else:
            print(f'{song.title} is already in Playlist.')

    def remove_song(self, title):
        songs_count = len(self.songs)
        # adding to all songs back self.songs except the song that must be removed.
        self.songs  = [song for song in self.songs if song.title != title]
        if songs_count == len(self.songs):
            print(f'Song {title} not found in Playlist.')
        else:
            print(f'{title} removed from Playlist.')

    def shuffle(self):
        shuffled = random.shuffle(self.songs)


    def all_songs(self):
        titles = [song.title for song in self.songs]
        print(f'Playlist:{' | '.join(titles)}')

playlist = Playlist('Divine Vibes')
playlist.add_song(Song("Om Mahaprana Deepam", "Shankar Mahadevan"))
playlist.add_song(Song("Bhagyada Lakshmi Baramma", "Rajeev & Sooryagayathri"))
playlist.add_song(Song("Lingashtakam", "SPB"))
playlist.add_song(Song("Ragvendra Raghavendra Yenniri", "Dr.Rajkumar"))


playlist.all_songs()
playlist.remove_song("Om Mahaprana Deepam")
playlist.shuffle()
print('After Shuffle:', end = ' ')
playlist.all_songs()
```