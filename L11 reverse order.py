n = int(input("enter a number: "))
temp = n
sum = 0

while temp > 0:
    sum = sum + 1
    temp = temp // 10 

print("the no of digits is ", sum)