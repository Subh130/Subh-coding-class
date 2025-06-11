from datetime import date, datetime

#Calling the today
#function of date class
today = date.today()
now = datetime.now()

print("today's date is ",today)
print("current date and time is", now)
print()

# Printing dates components
print("Date components", today.year, today.month, today.day)
print()