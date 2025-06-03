rowsize = int(input("enter the no of rows: "))

if rowsize % 2 == 0: #even row
    halfdiamrow= int(rowsize/2)
else: #odd row
    halfdiamrow = int(rowsize/2)+1

space = halfdiamrow-1

# Loop for upper part
for i in range(1, halfdiamrow+1): #loop for rows
    for j in range(1, space+1): #loop for column
        print(end=" ")

    space = space-1
    num = 1

    for j in range(2*i -1):
        print(end = str(num))
        num = num+1 #incrementing number at each column

    print()

space = 1 

#loop for lower part
for i in range(1, halfdiamrow): #loop for rows
    for j in range(1,space+1): #loop for column
        print(end=" ")

    space = space+1
    num = 1

    for j in range(1, 2*(halfdiamrow-i)):
        print(end = str(num))#displaying result
        num = num+1 #incrementing number at each column

    print()