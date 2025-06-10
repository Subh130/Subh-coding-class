valid = False

while not valid:
    try:
        n = int(input("Enter a number: "))

        #enter a even number
        if n%2 == 0: 
            print("even")
            valid =  True
        else:
            print("odd")

    except ValueError:
        print("Invalid")