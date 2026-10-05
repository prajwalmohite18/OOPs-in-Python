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
