##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import pandas as pd
with open("C:/Users/Rudraksh Sharma/Documents/100-days/Day 32/birthdays.csv", "r") as birthdays:
    birthday = pd.read_csv(birthdays)
    time = dt.datetime.now()
    today_date=time.day
    today_month=time.month
    for i in range(len(birthday)):
        date = birthday.day[i]
        month=birthday.month[i]
        name=birthday.name[i]
        if date == today_date and month==today_month:
            with open("C:/Users/Rudraksh Sharma/Documents/100-days/Day 32/letter_templates/letter_1.txt","r") as letter_1,open("C:/Users/Rudraksh Sharma/Documents/100-days/Day 32/letter_templates/letter_2.txt","r") as letter_2,open("C:/Users/Rudraksh Sharma/Documents/100-days/Day 32/letter_templates/letter_3.txt","r") as letter_3:
                wish_1,wish_2,wish_3=letter_1.read(),letter_2.read(),letter_3.read()
                letters=[wish_1,wish_2,wish_3]
                letter=random.choice(letters)
                letter=letter.replace("[NAME]",name)
            with smtplib.SMTP("smtp.gmail.com",587) as connection:
                connection.starttls()
                connection.login(user="pythonrudrsh01@gmail.com",password="mnsm bgsa gfct ckmq")
                connection.sendmail(from_addr="pythonrudrsh01@gmail.com",to_addrs=birthday.email[i],msg=f"Subject: Happy Birthday {name}!!\n\n{letter}")
