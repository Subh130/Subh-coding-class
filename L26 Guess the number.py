import random
import time

# Pick a number between 1 and 100
number = random.randint(1, 100)

def intro():
    print("May I ask you for your name?")
    global name
    name = input()  # asks for the name
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 100")

    if number % 2 == 0:
        x = "even"
    else:
        x = "odd"

    print(f"\nThis is an {x} number")
    time.sleep(0.5)
    print("Go ahead. Guess")

def pick():
    guesses_Taken = 0

    while guesses_Taken < 6:
        time.sleep(0.25)
        enter = input("Guess: ")

        try:
            guess = int(enter)
            if 1 <= guess <= 100:
                guesses_Taken += 1

                if guess < number:
                    print("The guess of the number that you have entered is too low")
                elif guess > number:
                    print("The guess of the number that you have entered is too high")
                else:
                    print(f"Good job, {name}! You guessed the number in {guesses_Taken} tries.")
                    return  # exit the function if guessed correctly

                if guesses_Taken < 6:
                    time.sleep(0.5)
                    print("Try Again!")
            else:
                print("Silly Goose! That number isn't in the range")
                time.sleep(0.25)
                print("Please enter a number between 1 and 100")
        except ValueError:
            print(f"I don't think '{enter}' is a number. Sorry.")

    if guess == number:
        guesses_Taken = str(guesses_Taken)
        print(f"Good job {name} you guessed the number in {guesses_Taken} guesses!")
    if guess != number:
        print("nope the number i was thinking of was "+ str(number))

playagain = "yes"
while playagain == "yes" or playagain == "y" or playagain == "Yes":
    intro()
    pick()
    print("do you want to play again?")
    playagain = input()           