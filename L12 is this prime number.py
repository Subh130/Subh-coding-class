# Take two input from the user
lower = int(input("Enter a lower range: "))
upper = int(input("Enter a upper range: "))

print()

print("prime numbers between", lower, "and", upper, "are:")

#displaying the result
for num in range(lower, upper+1):
    if num > 1: #all prime numbers are greater than one
        for i in range(2, num):
            if (num % i) == 0 :# if the number can be divided my other number it is not a prime number so we need to stop checking
                break
        else:
            print(num)
