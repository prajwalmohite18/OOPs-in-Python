# Exercise 5: Product Class with Stock Value Calculator
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return (self.quantity * self.price)

laptop = Product('Laptop', 50000, 10)
print('Product Name:', laptop.name, 'Product Price:',laptop.price, 'No of Products', laptop.quantity)
print('Total stock value of', laptop.name, 'is', laptop.total_value())
