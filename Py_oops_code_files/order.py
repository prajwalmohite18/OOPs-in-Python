# Exercise 20: Discounted Order Subclass with 10% Off

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