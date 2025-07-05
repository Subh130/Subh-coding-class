import random
class fruitQuiz:
    #create constructor
    def __init__(self):
        # create a dictionary of fruits as keys and color as values
        self.fruits = {'apple': 'red',
                       'grape': 'purple',
                        'watermelon': 'green',
                        'banana' : 'yellow',
                       }
    
    #function fo a quiz here a fruit will be chosen randomly
    def quiz(self):
        while(True):
            fruit, color = random.choice(list(self.fruits.items()))

            print("what is the color of {}".format(fruit))
            user_answer = input()

            if (user_answer.lower() == color):
                print("correct anser")
            else:
                print("Wrong anser")

            option = int(input("enter 0, if you want to play again otherwise 1: "))

            if (option):
                break

print("welcome to fruit quiz")
fq= fruitQuiz()
fq.quiz()