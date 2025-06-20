Lst_even = []
Lst_odd = []
original_list = []
fruit_list = ["mango", "apple", "guava", "grapes"]
def square(range_1):
    for i in range (range_1+1):
        original_list.append(i)
    for i in original_list:
        if i % 2 == 0:
            Lst_even.append(i)
        else:
            Lst_odd.append(i)

    print("the even numbers are:", Lst_even)
    print("the odd numbers are:", Lst_odd)
3
end = int(input("Enter the ending range: "))

square(end)

capitalized_fruits = [fruit.capitalize() for fruit in fruit_list]

print("the capitalized fruit is:", capitalized_fruits)