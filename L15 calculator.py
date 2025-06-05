def add(p, q):
    return p + q

def substract(p, q):
    return p - q

def multiply(p, q):
    return p * q

def divide(p, q):
    return p / q

print("please select operation")
print("a. Add")
print("b. Substract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter your choice (a/b/c/d): ")

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print()

if choice.lower() == "a": #convert input into lowercase letter and check if its 'a' letter
    result = add(num_1, num_2)
    print(num_1, "+", num_2, "=",result ) 

elif choice.lower() == "b":
    result = substract(num_1, num_2)
    print(num_1, "-", num_2, "=",result ) 

elif choice.lower() == "c":
    result = multiply(num_1, num_2)
    print(num_1, "*", num_2, "=",result ) 

elif choice.lower() == "d":
    result = divide(num_1, num_2)
    print(num_1, "/", num_2, "=",result ) 

else:
    print("it is an invalid input")