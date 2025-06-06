def factorial(n):
    if n == 0 or n == 1 :#Base case: 0! adn 1! are both 1 
        return 1
    else:
        return n * factorial(n - 1) # recursive call
    
num = int(input("enter a number: "))

# check if the number is negative

if num < 0:
    print("factorial does not exist for negative numbers")

else:
    result = factorial(num) #calling the function and saving the return value in variable
    print(f"The factorial of {num} is {result}")