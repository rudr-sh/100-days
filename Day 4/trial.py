import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))

options = ["🪨", "🗞️", "✂️"]

print(f"You cho0se \n {options[choice]}")
num_gen = random.randint(0,2)
computer = options[num_gen]
print(f"computer choose\n{computer}")

if choice == num_gen:
    print("This is a tie.")
elif (choice == 0 and num_gen == 2) or (choice == 1 and num_gen == 0) or (choice == 2 and num_gen == 1):
    print("You won.")
else:
    print("You lost.")    