# Exercise 26: Private Balance with Property Getter & Setter

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