print("Welcome to the tip calculator! ")

total_bill = int(input("What was the total bill? $"))
tip_amount = int(input("How much percentage of tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

final_amount = (total_bill)/(people) * ((1 + (tip_amount/100)))

print(round(float(final_amount)))