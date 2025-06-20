class parrot:
    #class attribute
    species = "bird"

    #instance attributes or constructor
    def __init__(self, nm, h):
        self.name = nm
        self.age = h

#create the object of the parrot class
blu = parrot("blue", 10)
woo = parrot("wooey", 15)

#access the class atributes
print(f"Blue is a {blu.species}")
print(f"Wooey is also a {woo.species}")

#access the instance attributes
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")