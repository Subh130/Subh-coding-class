def hotel_cost(nights):
    return 140*nights

#define a function called plane_ride_cost that takes a string city as input
def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
    elif "London" == city:
        return 275
    
#Define a function called rental_car_cost with an argument called days
def rental_car_cost(days):
    if days >= 7:
        return 40*days - 50
    elif days >= 3:
        return 40*days -20
    else:
        return 40*days 
    
#Define an function trip_cost with argument day, money and city
def trip_cost(city, days, money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + money

print("cost of car rental: ", rental_car_cost(6))

print("cost of plane ride: ", plane_ride_cost("Los Angeles"))

print("cost of hotel room: ", hotel_cost(7))

result = trip_cost("Los Angeles", 7, 500) #city, days and spending money
print("total cost of the trip to los angeles: ", result)