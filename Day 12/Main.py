import random
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty =input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
num = random.randint(1,100)
def tuff(user):
    if user > num:
        print("Too high.")
        attempts-=1
    elif user < num:
        print("Too low.")
        attempts-=1
    else:
        print(f"You guessed it correct, the number is {num}")
        attempts = 0
    return
def easy(user):
    if user > num:
        print("Too high")
        attempts-=1
    elif user < num:
        print("Too low.")
        attempts-=1
    else:
        attempts = 0
    return
if difficulty =="easy":
    attempts = 10
    while attempts > 0:
        print(f"You have {attempts} guess remaining to guess the number.")
        enter = int(input("Make a guess: "))
        easy(enter)
elif difficulty =="hard":
    attempts = 5
    while attempts > 0:
        print(f"You have {attempts} guess remaining to guess the number.")
        enter = int(input("Make a guess: "))
        tuff(enter)
else:
    print("You have entered wrong answer.")
