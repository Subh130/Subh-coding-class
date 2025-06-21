class IOString(): 
    #Constructor to set default value
    def __init__(self):
        self.str1 = ""

    #method to get input from user
    def get_string(self):
        self.str1 = input("enter string: ")

    #method to print string in upper case
    def print_string(self):
        print("result is: ", self.str1.upper())

#Object creation
str_object = IOString()

#Call method 
str_object.get_string()
str_object.print_string()