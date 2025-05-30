# input the word or sentence 
string = input("Please enter your own string: ")

reverse = ("")

# loop for printing n reverse
for i in string:
    reverse = i + reverse 

print()

print("the original string is: " ,string)
print("the reverse string is: ", reverse)
