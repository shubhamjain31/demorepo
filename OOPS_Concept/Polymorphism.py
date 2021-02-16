'''class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am dog. My name is {self.name}. I am {self.age} years old.')

    def sound(self):
        print('bow bow')

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am cat. My name is {self.name}. I am {self.age} years old.')

    def sound(self):
        print('meow meow')

c = Cat('Kitty', 2.3)
d = Dog('Rambo', 4)

for animal in (c, d):
    animal.sound()
    animal.info()
    animal.sound()'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am dog. My name is {self.name}. I am {self.age} years old.')

    def sound(self):
        print('bow bow')

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am cat. My name is {self.name}. I am {self.age} years old.')

    def sound(self):
        print('meow meow')

#common interface
def sound_test(animal):
    animal.sound()
    animal.info()

#instantiate objects
c = Cat('Kitty', 2.3)
d = Dog('Rambo', 4)

#passing the object
sound_test(c)
sound_test(d)