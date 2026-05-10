
with open("C:/Users/Rudraksh Sharma/Documents/100-days/Day 24/Names/names.txt",mode="r") as names:
    list_names = names.readlines()
for i in list_names:
    i=i.strip()
    with open("C:/Users/Rudraksh Sharma/Documents/100-days/Day 24/Input/starting_letter.txt",mode="r") as letter:
        new_letter=letter.read()
        final_letter=new_letter.replace("[name]",f"{i}")
    with open(f"C:/Users/Rudraksh Sharma/Documents/100-days/Day 24/Output/{i}_letter.txt",mode="w") as invite:
        invitation=invite.write(final_letter)
