L = [4, 5, 1, 2, 9, 7, 10, 8]

print("original list :", L)
print()

count = 0 

for i in L:
    count = count + i
    
avg = count/len(L)

print("sum", count)
print("average", avg)
print()

# sorting the elements of list
L.sort()
print("sorted array in ascending order: ", L)
print()

#print the first element
print("the smallest element is:", L[0])
print()

# printing the last element
print("the largest element is:", L[-1] )