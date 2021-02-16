class Employee:

    #class variable
    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):

        #instance variable
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1

    def increase(self):
        self.salary = int(self.salary * self.increment)

    def display(self):
        print('Salary of {} is {}'.format(self.fname ,self.salary))

#object 1
emp1 = Employee('Shubham', 'Jain', 20000)
emp1.increase()
emp1.display()

#object 2
emp2 = Employee('Mohammad', 'Danish', 22000)
emp2.increase()
emp2.display()

print(Employee.no_of_employees)