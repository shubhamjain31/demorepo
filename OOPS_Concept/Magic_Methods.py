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

    #Magic methods Or Dunder methods
    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return 'Employee({} {} {})'.format(self.fname, self.lname, self.salary)

    def __str__(self):
        return 'The name of employee is {}'.format(self.fname)

emp1 = Employee('Shubham', 'Jain', 20000)
emp2 = Employee('Mohammad', 'Danish', 22000)

print(emp1)
print(repr(emp1))
print(emp1 + emp2)