#my code
import random

name_string = input("Give me everybody's names, seperated by a comma. ")
names = name_string.split(", ")

select = random.choice(names)

print(f"{select} needs to pay the bill")
