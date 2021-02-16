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

    #static method
    @staticmethod
    def isopen(day):
        if day == 'Sunday':
            return False
        else:
            return True

emp1 = Employee('Shubham', 'Jain', 20000)

print(emp1.isopen("Sunday"))