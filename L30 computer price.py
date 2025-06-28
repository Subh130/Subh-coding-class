class Computer:
    def __init__(self):#constructor
        self.__maxprice = 900 #private variable

    def sell(self):
        print(f"Selling price: {self.__maxprice}")

    def setMaxPrice(self,price):
        self.__maxprice = price

#create object
c = Computer()
print("original price")
c.sell()
print()

#change the price
print("after try to change it directly")
c.__maxprice = 1000
c.sell()
print()

#using setter function
print("change it using setMaxPrice method")
c.setMaxPrice(1500)
c.sell()