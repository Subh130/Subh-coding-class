import os

shutdown = input("do you wish to shutdown your computer? (yes or no): ")

if shutdown.lower() == "no":
    exit()
elif shutdown.lower() == "yes": 
    os.system("shutdown /s /t 1")
else:
    print("invalid input")