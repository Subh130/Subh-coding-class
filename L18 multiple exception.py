try:
    num1, num2 = eval(input("enter two numbers seperated by comma: "))
    result = num1/num2
    print("result is:", result)
    print("result is:", result1) #this is error

except ZeroDivisionError:
    print("division by 0 is not allowed")

except SyntaxError:
    print("comma is missing. Enter numbers seperated like this: 1, 2")

except ValueError:
    print("please enter numerical value")

except NameError as ex:
    print("The exception is", ex)

except:
    print("some error occured ")

else:
    print("no exception or no error")

finally:
    print("I will execute no matter what happens")
    print()