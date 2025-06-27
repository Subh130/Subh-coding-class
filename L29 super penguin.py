class Bird: #parent class
    def __init__(self):
        print("bird is ready")

    def whoisThis(self):
        print("bird")
    
    def swim(self):
        print("swim faster")

#child class
class Penguin(Bird):
    def __init__(self):
        #call Super() function
        super().__init__()
        print("penguin is ready")

    def whoisThis(self):
        print("penguin")

    def run(self):
        print("run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()