class vehicle: #parent class
    def __init__(self, nm, speed, mile):
        self.name = nm
        self.maxspeed = speed
        self.milage = mile

class Bus(vehicle):
    pass

school_bus = Bus("School Volvo", 180, 12)

print("Vehicle name:", school_bus.name,"\nMax speed:", school_bus.maxspeed, "\nMilage:", school_bus.milage)