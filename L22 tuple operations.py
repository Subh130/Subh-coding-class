# create tuple with different variables
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)
print()

#create a numeric tuple
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
#tuples are immutable so you cannot add new elements
print()

#using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9, )
print(tuplex)
print()

# count the no of occurence of item 50 from the tuple
tuplel = (50, 10, 50, 70, 50)
print(tuplel.count(50))
print()

#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

#using tuple [start:stop] the start index is inclusive and the stop index is exclusive
_slice  = tuplex[3:5]
print(_slice)
print()

#If the start value isent defint it is taken from the begining of the tuple
_slice = tuplex[:6]
print(_slice)