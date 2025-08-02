#Love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

#True
TRUE =str(name1.count("t") + name2.count("t") + name1.count("r") + name2.count("r") + name1.count("u") + name2.count("u") + name1.count("e") + name2.count("e")) 
#Love
LOVE =str(name1.count("l") + name2.count("l") + name1.count("o") + name2.count("o") + name1.count("v") + name2.count("v") + name1.count("e") + name2.count("e"))

Love_Score = int(TRUE + LOVE)

if Love_Score <= 10 or Love_Score>=90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif 40<=Love_Score<=50:
    print(f"Your score is {Love_Score}, you are alright together.")
else:
    print(f"Your score is {Love_Score}.")
