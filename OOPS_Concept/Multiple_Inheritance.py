class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showName(self):
        print('Name is {}'.format(self.name))

    def showAge(self):
        print('Age is {}'.format(self.age))

class Student:
    def __init__(self, studentId):
        self.studentId = studentId

    def getId(self):
        return self.studentId

    def showId(self):
        print('Student ID is {}'.format(self.studentId))

class Resident(Person, Student):
    def __init__(self, name, age, id):
        Person.__init__(self, name, age)
        Student.__init__(self, id)

r1 = Resident('Shubham', 26, 102)
r1.showName()
r1.showAge()
r1.showId()