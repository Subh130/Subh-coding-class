import math

print("The floor value of 23.65 is: "+ str(math.floor(23.65)) )
print("The ceil value of 23.65 is: "+ str(math.ceil(23.65)) )
print()

x = 10
y = -15

print("The value of x after copying the sign from y is: " + str(math.copysign(x,y)))
print()

#Using fabs and gcd function

print("absolute value of -96 and 56 are: "+ str(math.fabs(-96)) + ", " + str(math.fabs(56)))
print()

print("the GCD of 24 and 56 are: "+ str(math.gcd(24,56)))
print()

print("sin, cos and tan of 45:")
print(math.sin(45))
print(math.cos(45))
print(math.tan(45))

print()
print("the factorial of 5: " +str(math.factorial(5)))