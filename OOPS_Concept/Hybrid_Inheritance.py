class School:
    def show(self):
        print('This is for School !')

class Student_Ram(School):
    def show_Ram(self):
        print('This is for Student Ram !')

class Student_Vijay(School):
    def show_Vijay(self):
        print('This is for Student Vijay !')

class Student_Mahesh(Student_Ram, Student_Vijay):
    def show_Mahesh(self):
        print('This is for Student Mahesh !')

s1 = Student_Mahesh()
s1.show_Ram()
s1.show_Vijay()
s1.show_Mahesh()