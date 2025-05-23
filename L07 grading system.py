print("enter marks obtained in 5 subjects: ")
markone = int(input())
marktwo = int(input())
markthree = int(input())
markfour = int(input())
markfive = int(input())

tot = marktwo + marktwo + markthree + markfour + markfive
avg = tot/5

if 91 <= avg and avg <= 100:
    print(" your grade is A1 ")
elif 81 <= avg and avg < 91:
    print(" your grade is A2 ")
elif 71 <= avg and avg < 81:
    print(" your grade is B1 ")
elif 61 <= avg and avg < 71:
    print(" your grade is B2 ")
elif 51 <= avg and avg < 61:
    print(" your grade is C1 ")
elif 41 <= avg and avg < 51:
    print(" your grade is C2 ")
elif 33 <= avg and avg < 41:
    print(" your grade is D ")
elif 21 <= avg and avg < 33:
    print(" your grade is E1 ")
elif 0 <= avg and avg < 21:
    print(" your grade is E2 ")
else:
    print("invalid input!")