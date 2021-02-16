class Details:
    def __init__(self):
        self.__id = ''
        self.__name = ''
        self.__gender = ''

    def setData(self, id, name, gender):
        self.__id = id
        self.__name = name
        self.__gender = gender

    def showData(self):
        print("ID:",self.__id)
        print("Name:",self.__name)
        print("Gender:",self.__gender)

class Employee(Details):
    def __init__(self):
        self.__company = ''
        self.__dept = ''

    def setEmployee(self, id, name, gender, company, department):
        self.setData(id, name, gender)
        self.__company = company
        self.__dept = department

    def showEmployee(self):
        self.showData()
        print("Company:",self.__company)
        print("Department:",self.__dept)

class Doctor(Details):
    def __init__(self):
        self.__hospital = ''
        self.__dept = ''

    def setEmployee(self, id, name, gender, hos, department):
        self.setData(id, name, gender)
        self.__hospital = hos
        self.__dept = department

    def showEmployee(self):
        self.showData()
        print("Hospital:",self.__hospital)
        print("Department:",self.__dept)

e = Employee()
e.setEmployee(1, 'Shubham', 'Male', 'Ravi Corporation', 'CEO')
e.showEmployee()

d = Doctor()
d.setEmployee(1, 'Ram', 'Male', 'Ram Clinic', 'eyes')
d.showEmployee()