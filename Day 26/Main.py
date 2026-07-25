import pandas
data = pandas.read_csv("C:/Users/Rudraksh Sharma/Documents/100-days/Day 26/nato_phonetic_alphabet.csv")
dict_names={row.letter:row.code for (index,row) in data.iterrows()}
name=input("Enter your name: ")
list_name=[letter.upper() for letter in name]

final_list=[dict_names[name] for name in list_name]
print(final_list)
