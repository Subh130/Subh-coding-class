#Take input for the student that he can attend the exam or not
medical_cause = input("Do you have a medical casue Y or N: ")

#Take input of attendance
atten = int(input("enter the attendance of the student: "))

if medical_cause == "Y": #Checking the condition 1
    print("You are allowed ")
else:
    if atten >= 75: #checking the condition 2
        print("allowed")
    else:
        print("Not allowed")