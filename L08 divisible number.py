numn = int(input("Enter a number (Numerator): "))
numd = int(input("Enter a number (denominator): "))

print()

if numn % numd == 0:
    print(f"{numn} is divisible by {numd}")
else:
    print(f"{numn} is not divisible by {numd}")