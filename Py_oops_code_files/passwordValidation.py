# Exercise 8: User Class with Password Validation
class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password
        
user1 = User('shyam', 'shyam123')
print(user1.check_password('shyam123'))
print(user1.check_password('shyam1234'))
