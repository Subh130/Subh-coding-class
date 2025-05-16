# Take marks input from user
print("enter marks obtained in 3 subjects: ")

math = int(input("math: "))
english = int(input("english: "))
science = int(input("science: "))

#lets calculate percentage of marks
sum= math+english+science
print("sum of maths english and science: ", sum)

perc = (sum/300)*100
print(f"the percentage is: {perc}")