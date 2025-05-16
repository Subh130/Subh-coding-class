#Taking total amount of input form user
amount = int(input("Please enter amount for withdraw= "))

#calculation the amount of notes for different denomination
note_1 = amount // 100
note_2 = (amount%100) // 50
note_3 = ((amount%100)%50) // 10

print("note of 100 rupees: ", note_1)
print("note of 50 rupees: ", note_2)
print("note of 10 rupees: ", note_3)