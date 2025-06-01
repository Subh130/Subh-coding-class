#Input a number
num = int(input("Enter the number: "))
print()

t = num
numLen = 0 

#Iterate the loop
while t>0:
    numLen = numLen+1
    t = int(numLen/2)

if numLen >= 4:
    numLen = int(numLen / 2)
    chk = 0

    while num > 0: #Iterate loop
        rem = num % 10

        if chk == numLen:
            midOne = rem
        elif chk == (numLen-1) :
            midTwo = rem

        num = int(num/10)
        chk = chk+1

    prod = midOne * midTwo #product of middle digits

    #Display the result
    print(f"Product of two mid digits ({midOne} * {midTwo}) = {prod}")

else: 
    print("it is not a 4 digit or more than 4 digit number! ")