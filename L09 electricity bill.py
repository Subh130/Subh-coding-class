# Take input of no of units consumed by the user 
units = int(input("Enter the no of units you consumed: "))

#Check conditions of unit consumed
#Then calculate the surcharge accordingly
# surcharge is the tax value 

if(units < 50): # Check for units less than 50
    amount =  units * 2.60
    surcharge = 25

elif(units <= 100): # Check for units less than 100
    amount = 130 + ((units-50) * 3.25)
    surcharge = 35

elif(units <= 200): # Check for units less than 200
    amount =  130 + 162.50 + ((units-100) * 5.26)
    surcharge = 45

# Check for all the cases other than mentioned
#When units are consumed more than 200

else:
    amount = 130 + 162.50 + 526 + ((units-200) * 8.45)
    surcharge = 75

#Calculate and display the total electricity bill
#Total amount = amount + surcharge
total = amount + float(surcharge)
print(f"Electricity bill is: {total}")