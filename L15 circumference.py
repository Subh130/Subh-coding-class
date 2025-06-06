def circumference (r):
    circumference = 2 * (22/7) * r
    return circumference

r = float(input("enter the radius: "))

value = circumference(r)
print(f"The circumference of the circle is {value}")