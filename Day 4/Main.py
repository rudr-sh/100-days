import random
print("Welcome to coin tosser.")

start = input("Do you want to toss a coin? Y or N\n").lower().strip()

if start == "y":
    random_int = random.randint(0,1)
    if random_int == 0:
        print("You got tails.")
    else:
        print("You got a head.")
