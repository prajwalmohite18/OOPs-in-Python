# Exercise 20: Discounted Order Subclass with 10% Off
class Order():
    def __init__(self,id, total):
        self.id = id
        self.total = total

    def get_total(self):
        return self.total

class DiscountOrder(Order):
    def __init__(self, id, original):
        super().__init__(id, original)

    def get_total(self):
        return self.total - self.total * 0.9
      

o1 = DiscountOrder('OR001', 1200)
o2 = DiscountOrder('OR002', 1000)

print(f'Order ID: {o1.id}\nOriginal Total: {o1.total}\nDiscounted Total: {o1.get_total()}')
print(f'Order ID: {o2.id}\nOriginal Total: {o2.total}\nDiscounted Total: {o2.get_total()}')
o1.total = 100
print(o1.total, o1.get_total())