class myClass:
    #private variable
    __privatevar = 27

    #private method
    def __privMeth(self):
        print("I'm inside class Myclass")

    #function to print the private variable
    def hello(self):
        print("Private variable value: ", myClass.__privatevar )

#object creation and method call
foo = myClass()
foo.hello()
foo.__privMeth() #this will give error bacause private cannot be accessed