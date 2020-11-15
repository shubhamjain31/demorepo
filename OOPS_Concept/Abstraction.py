from abc import ABC, abstractmethod

class Shape(ABC):

    #concreate method
    def common(self):
        print('This is a concreate method')

    #two abstract methods
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side*self.__side

    def perimeter(self):
        return 4*self.__side

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length*self.__breadth

    def perimeter(self):
        return 2*(self.__length + self.__breadth)

s1 = Square(4)
print(s1.common())
print(s1.area())
print(s1.perimeter())

r1 = Rectangle(2, 4)
print(r1.common())
print(r1.area())
print(r1.perimeter())