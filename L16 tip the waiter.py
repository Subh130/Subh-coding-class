def total_calc(bill_amount, tip_perc):
    total = bill_amount*(1 + 0.01 * tip_perc)
    total = round(total,2)

    print(f"Please pay ${total}")

bill = 150
tip = 20
total_calc(bill,tip)# passing argument bill and tip