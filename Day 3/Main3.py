#Welcome to BMI calculator 2.0
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in Kg: "))

BMI = float(round(weight / height ** 2,2))

if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI<= 25:
    print(f"Your BMI is {BMI}, your weight is normal.")
elif BMI<= 30:
    print(f"Your BMI is {BMI}, you are overweight.")
elif BMI <= 35:
    print(f"Your BMI is {BMI}, You are obese.")
else:
    print(f"Your BMI is {BMI}, You are clinically obese.")

user_response=(input("Thanks for using our BMI calculator. Are you satisfied with our program?(Yes,No) "))

if user_response == "Yes":
    print("Thanks for using our program")

else:
    feedback = input("Please share your concerns...\n")
    
