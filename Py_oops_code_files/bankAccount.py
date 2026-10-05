# Exercise 6: Bank Account with Deposit & Overdraw Protection
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