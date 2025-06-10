import random

options = ["Rock",  "Paper", "Scissors"]
user_choice = input("Choose Rock, Paper, Scissors: ")
computer_choice = random.choice(options)
print()

print("you choose", user_choice)
print("computer choose", computer_choice)

if user_choice == computer_choice:
    print("Its a tie")

elif user_choice == "Rock" and computer_choice == "Scissors":
    print("rock smashes scissors! you win")

elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers rock! you win")

elif user_choice == "Scissors" and computer_choice == "Paper":
    print("scissors cuts paper! you win")

else:
    print("you lose!. ")