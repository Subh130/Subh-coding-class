from abc import ABC, abstractmethod

#Create parent class
class Absclass(ABC):
    #function to print a value
    def display(self,x):
        print("passed value:", x)

    #abstract method
    @abstractmethod
    def task(self):
        print("we are inside Absclass task")

#create subclass/ child class
class test_class(Absclass):
    def task(self):
        print("we are inside test_class task")

#object of test class method
test_obj = test_class()

test_obj.task()
test_obj.display(100)