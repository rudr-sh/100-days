import pandas
data = pandas.read_csv("C:/Users/Rudraksh Sharma/Documents/100-days/Day 26/nato_phonetic_alphabet.csv")
dict_names={row.letter:row.code for (index,row) in data.iterrows()}
def generate_phonetic():    
    name=input("Enter your name: ")
    try:
        list_name=[letter.upper() for letter in name]
        final_list=[dict_names[name] for name in list_name]
        print(final_list)

    except KeyError:
        print("Invalid input, only english alphabets are allowed.")
        generate_phonetic()
generate_phonetic()