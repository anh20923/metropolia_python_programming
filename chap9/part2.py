class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

class Dog(Animal):
    def bark(self):
        print(self.name, "is barking")



dog = Animal("Buddy")
dog.eat()

my_dog = Dog("Max")
my_dog.eat()
my_dog.bark()