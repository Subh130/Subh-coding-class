#Adding two lists using map and lambda
numbers1 = [1,2,3]
numbers2 = [4,5,6]

result = map(lambda x, y: x+y, numbers1, numbers2)

print("addition of two lists")
print(list(result))

print()

#Using map
nums = [1,2,3,4,5]

def pow(n):
    return n*n

square = list(map(pow, nums))
print("square of numbers in list")
print(square)