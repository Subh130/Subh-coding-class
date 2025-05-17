n = int(input("enter the number: "))

if n <= 15:
    print(f"{n} is smaller than or equal to 15")
    print("I'm in the IF block")

else:
    print(f"{n} is greater than 15 ")
    print("I'm in the ELSE block")

print("I'm not in the IF block and I'm not in the ELSE block")