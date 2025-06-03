print("Half pyramid pattern of the stars (*)")
n = int(input("Enter the no of rows: "))

for i in range(n): #outer loop to handle no or rows
    for j in range(i+1): #inner loop to handle no of colums
        print("* ", end="") #display result

    print()
