#Welcome to rock paper scissors
#Start
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))

options = ["🪨", "🗞️", "✂️"]
if choice == 0:
    print('You chose 🪨')
    computer = random.choice(options)
    print(f"Compter choose {computer}")
    if computer == "🪨":
        print("This is a tie")
    elif computer == "🗞️":
        print("You lost.")
    else:
        print("You won.")
elif choice == 1:
    print("You choose 🗞️")
    computer = random.choice(options)
    print(f"Compter choose {computer}")
    if computer == "🗞️":
        print("This is a tie")
    elif computer == "🪨":
        print("You won")
    else:
        print("You lost.")
else:
    print("You choose ✂️")
    computer = random.choice(options)
    print(f"Compter choose {computer}")

    if computer == "✂️":
        print("This is a tie.")
    elif computer == "🗞️":
        print("You won.")
    else:
        print("You lost.")
#Done    
