#define the function to calculate cube
def cube(number):
    return number * number * number

#define a function which will execute cube function if the user entered number is divisible by 3
def by_three(num):
    if num % 3 == 0:
        return cube(num) #calling function cube()
    else:
        return False
    
x = 9
y = 4

#Display result
result_1 = by_three(x) #passing argument x
result_2 = by_three(y) #passing argument y

print(result_1)
print(result_2)