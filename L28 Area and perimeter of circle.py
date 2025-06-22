class circle:
    def __init__(self, r):
       print("The area is", area(r))
       print("The perimeter is", area(r))

def  area(r):
    A = (22/7) *r*r
    return A

def perimeter(r):
    P = 2 * (22/7) *r
    return P

r = int(input("enter the radius: "))
value = circle(r)
print(circle)
