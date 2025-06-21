class Employee:
    #initial constructor
    def __init__(self):
        print("Employee created")

    #calling destructor
    def __del__(self):
        print("Destructor called")

#function outside the class
def create_obj():
    print("making object")
    obj = Employee()
    
    print("function end")
    return obj

print("calling create_obj function")
object_1 = create_obj()

print("program end")