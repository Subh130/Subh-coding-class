alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
u_alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M", "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

import random

password = ""

for i in range (2):
    password = password + str(random.randint(0,10))
    password = password + random.choice(alphabets)
    password = password + random.choice(u_alphabets)
    password = password + str(random.randint(0,10))

print("your password is: ", password)