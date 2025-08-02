#This program tells you if a year is leap or not
print("Lets find out if a year is leap or not.")
year = int(input("What year do you choose? "))

if year % 4 == 0:
    if year % 100 == 0:
         if year % 400 == 0:
              print("Yes, your selected year is a leap year.")
         else:
              print("This is not a leap year.")
    else:
         print("Yes, your selected year is a leap year.")
else:
     print("This is not a leap year.")
                     
        