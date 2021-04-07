class Animal():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    
class Dog(Animal):

    def info(self):
        print(("My name is {name} and I am {age} years old").format(name = self.name, age = self.age))
        a = 10
        print(a) 


    def sound(self):
        print("Bow")

class Cat(Animal):

    def info(self):
        print(("My name is {name} and I am {age} years old").format(name = self.name, age = self.age))

        
    def sound(self):
        print("Meow")


myCat = Cat('Thea', 2.5)
myDog = Dog('Robert', 6)

for animal in (myCat, myDog):
    animal.sound()
    animal.info()