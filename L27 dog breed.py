class dog:
    def __init__(self, nm, h):
        self.name = nm
        self.age = h

gol = dog("Golden retriver", 10)
hus = dog("Huskey", 8)

print(f"{gol.name} is {gol.age} years old")
print(f"{hus.name} is {hus.age} years old") 