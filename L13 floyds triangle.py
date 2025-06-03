rows = int(input("Enter the total no of rows: "))
number  = 1 #initialize by 1 

print("Floyd's triange")

for i in range(1, rows+1): #representing rows
    for j in range(1, i+1): #representing columns
        print(number , end="  ")
        number = number + 1 

    print()