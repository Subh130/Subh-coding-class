class vehicle:
    def __init__(self, nm, fare):
        self.name = nm
        self.busfare = (fare/10)*15

class Bus(vehicle):
    pass

school_bus = Bus("School Volvo", 25)

print("Vehicle name:", school_bus.name,"\nBus Fare:", "$"+ str(school_bus.busfare) )