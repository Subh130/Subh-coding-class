from abc import ABC

#create a base class / child class
class Animal(ABC):
    #should be implemented by all sub classes
    def move(self):
        pass

#Sub classes / child classes
class Human(Animal):
    def move(self):
        print("i can walk and run")

class snake(Animal):
    def move(self):
        print("i can crawl")

class Dog(Animal):
    def move(self):
        print("i can bark")

class Lion(Animal):
    def move(self):
        print("i can roar")

#create object
r = Human()
r.move()

k = snake()
k.move()

x = Dog()
x.move()

y = Lion()
y.move()