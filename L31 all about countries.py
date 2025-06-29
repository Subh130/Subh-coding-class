class Nepal():
    def capital(self):
        print("the capital of Nepal is Kathmandu")

    def language(self):
        print("the national language of Nepal is Nepali")

    def type(self):
        print("it is a developing country")

#class 2
class USA():
    def capital(self):
        print("the capital of USA is Washington D.C")

    def language(self):
        print("the national langue of USA is English")

    def type(self):
        print("it is a developed country")

#object creation
obj_Nep = Nepal()
obj_usa = USA()

#common interface
for country in (obj_Nep, obj_usa):
    country.capital()
    country.language()
    country.type()
    print()