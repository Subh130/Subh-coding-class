import array as arr

#crate an array
array_num = arr.array('i', [1,3,5,3,7,9,3] )
print("original array: "+ str(array_num))
print()

#Count the no of occurences
print("Number of occurences of no 3 in the said array: "+ str(array_num.count(3)))
print()

#reverse the array
array_num.reverse()
print("Reverse the order of items: ")
print(str(array_num))