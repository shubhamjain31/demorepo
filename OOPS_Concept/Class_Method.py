class Employee:

    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1

    def increase(self):
        self.salary = int(self.salary * self.increment)

    def display(self):
        print('Salary of {} is {}'.format(self.fname ,self.salary))

    #class method
    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

emp1 = Employee('Shubham', 'Jain', 20000)
emp2 = Employee.from_str("Mohammad-Danish-22000")

print(emp2.fname +' ' + emp2.lname)
print(Employee.no_of_employees)