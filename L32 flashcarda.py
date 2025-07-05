class flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        #we will return a string
         return self.word+" ( "+self.meaning+ " )"

flash = []
print("welcome to flashcard application:")

#The loop will be repeated until the user stops and adds a flashcard
while(True):
    word = input("enter name you want to add to the flash card: ")
    meaning = input("enter the meaning of the word: ")

    flash.append(flashcards(word, meaning))
    option = int(input("enter 0, if you want to enter another flashcard othewise 1 : "))

    if(option):
        break

print()
#print all the flashcards
print("Your flashcards")
for i in flash:
    print(">", i)