#set of integers
my_set = {1,2,3}
print(my_set)
print()

#Set of mixed data types
my_set = {1.0, "hello", (1,2,3)}
print(my_set)
print()

#set cannot have duplicates
my_set = {1,2,3,4,3,2}
print(my_set)
print()

#we can make set from a list
my_set = set([1,2,3,2])
print(my_set)
print()

#remove a number from a set
num_set = {0,1,3,4,5}
print("original set")
print(num_set)
print()

num_set.pop()
print("after removing the first element from the set: ")
print(num_set)