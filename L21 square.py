Lst_even = []
Lst_odd = []
original_list = []

def square(range_1, range_2):
    for i in range (range_1, range_2):
        original_list.append(i**2)
    for i in original_list:
        if i % 2 == 0:
            Lst_even.append(i)
        else:
            Lst_odd.append(i)

    print("the even numbers are:", Lst_even)
    print("the odd numbers are:", Lst_odd)
3
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

square(start, end)