#This is your days left to live

age = input("What is your current age? ")

left_years = 90 - int(age)

num_months = left_years * 12
num_weeks = left_years * 52
num_days = left_years * 365

print(f"You have {num_days} days, {num_weeks} weeks and {num_months} left.")
