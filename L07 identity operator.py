#Python program to illustrate the use
# of 'is' identity operator
x = 5
if (type(x) is int):
    print("true")
else:
    print("false")

x=5.0 
if (type(x) is not float):
    print("true")
else:
    print("false")

x = 20
y = 20
if (x is y):
    print("x and y same identity")

a = 20
b = 30
if (a is not b):
    print("a and b have DIFFERENT identity")