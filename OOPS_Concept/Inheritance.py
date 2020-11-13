class Employee:

    increment = 1.5
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * self.increment)

    def display(self):
        print('Name of Employee is {} {}'.format(self.fname ,self.lname))
        print('Salary of Employee is {}'.format(self.salary))
        print('{} has {} months experience in {}'.format(self.fname ,self.experience, self.proglang))

class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, experience):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.experience = experience

p1 = Programmer('Shubham', 'Jain', 20000, 'Python', 6)
p1.increase()
p1.display()