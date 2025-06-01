#Take input of word
string = input("Enter your own word or sentence: ")\

# Take input of Character
char = input("Enter your own character: ")

i = 0
count = 0

#Loop will find the occurence of character
while(i < len(string)): #string operation
    if (string[i] == char): #Check each letter of the word to find if its the same as the character we want to find
        count = count + 1

    i = i+1 #increase the value of i until it reaches the value of the length of the word i is the position of each letter in the word

# Display the result
print(f"The total number {char} character occured {count} times")