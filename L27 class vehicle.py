class vehicle:
    #create init method using constructor
    def __init__(self, speed, mile):
        #Bind the arguments
        self.max_speed = speed
        self.mileage = mile

#object creation
bike = vehicle(240, 18)

car = vehicle(300, 12)

#access the variables inside the init method
print("bike Max speed:", bike.max_speed)
print("bike Mileage:", bike.mileage)

print()

print("car Max speed:", car.max_speed)
print("car Mileage:", car.mileage)