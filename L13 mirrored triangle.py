rows = int(input("enter the no of rows: "))

for i in range (1,rows+1):
    for j in range (rows-i):
        print("  ", end="")

    
    for j in range (i):
        print( "* ", end= "")
    print()