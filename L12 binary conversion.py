num = int(input("enter a number: "))
binary = ""

while num > 0:
    binary = str(num%2) + binary
    num = num // 2

print("The binary number is: ", binary) 