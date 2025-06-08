price = 400
money = int(input("enter the amount given by the costumer: "))

def change(money):
    change = money - price
    return change

value = change(money)
print("the change is",value)