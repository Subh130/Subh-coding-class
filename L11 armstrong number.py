# take input from the user
num = int(input("Enter a number: "))

#initialize the sum
sum = 0 

#Find the sum of cube of each digits
temp = num

while temp > 0: 
    digit = temp % 10 # Getting the remainder of the division
    sum = sum + digit ** 3 # Calculate the each digit to the power of 3 and calculate the sum
    temp = temp // 10 #floor division (The result is rounded down by each decimal value)

#Display the result 
if num == sum:
    print(num, " is an armstrong number")
else:
    print(num, " is not an armstrong number")