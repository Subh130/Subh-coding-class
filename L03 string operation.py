#input a word
text = str(input("Enter a string: "))

#reverse string
#using step value as -1 to iterate in reverse
revtext = text[::-1]
text = revtext

print("the reverse text is: ")
print(text)