class BMW():
    def fuel_type(self):
        print("the fuel type of BMW is Petrol")

    def max_speed(self):
        print("the max speed of BMW is 350 km/h")

class Mercedes():
    def fuel_type(self):
        print("the fuel type of Mercedes is Petrol")

    def max_speed(self):
        print("the max speed of Mercedes is 330 km/h")

class Bugatti():
    def fuel_type(self):
        print("the fuel type of Bugatti is Petrol")

    def max_speed(self):
        print("the max speed of bugatti is 490 km/h")

obj_BMW = BMW()
obj_Mercedes = Mercedes()
obj_Bugatti = Bugatti()

for vheicle in (obj_BMW, obj_Mercedes, obj_Bugatti):
    ()
    vheicle.fuel_type()
    vheicle.max_speed()
    print()