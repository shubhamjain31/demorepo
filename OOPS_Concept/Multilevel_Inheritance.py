#class 1
class Family:
    def show_family(self):
        print('This is our family')

#class 2
class Father(Family):
    fname = ''
    def show_father(self):
        print(self.fname)

#class 3
class Mother(Family):
    mname = ''
    def show_mother(self):
        print(self.mname)

#class 4
class Son(Father, Mother):
    def show_parent(self):
        print("Father: ",self.fname)
        print("Mother: ",self.mname)

s1 = Son()
s1.fname = 'Ravi'
s1.mname = 'Anita'
s1.show_family()
s1.show_parent()