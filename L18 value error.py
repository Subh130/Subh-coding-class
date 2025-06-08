try:
    #num = int(input("Enter your number: "))
    print("the number entered is:", num)

except NameError as e: #using name error
    print("exception: ", e)

print("I am outside the try except block") #always executed and displayed the message
print()