print("select your ride")
print("1.Bike")
print("2.Car")

choice = int(input("Enter your choice (1 or 2): "))

if(choice == 1 ): # Conditon 1 outer if statement
    print("What type of bike? ")
    print("1.scooty\n")
    print("2.scooter\n")

    # Condition for selecting the type of bike
    choice2 = int(input("enter your choice2 (1 or 2): "))
    if choice2 == 1: #Inner if
        print("you have selected scooty")
    else:
        print("you have selected scooter")


elif (choice == 2): #outer elif statement
    print("what type of car?")
    print("1.Sedan")
    print("2.XUV")

    choice3 = int(input("enter your choice: "))

    if choice3 == 1: #inner if statement
    #Condition of selection type of car
        print("you have selected sedan")
    else:
        print ("you have selected XUV")

else: #outer else statement
    print("wrong choice")
