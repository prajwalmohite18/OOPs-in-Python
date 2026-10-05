# Exercise 17: Full-Time vs Part-Time Employee Pay Logic

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
        