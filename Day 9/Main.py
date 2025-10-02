import logo
full ='yes'
bidders = {}
def auction(name,money):
        bidders[name] = money    
while full == 'yes':
    print(logo.logo)
    print("Welcome to the secret auction program.")
    Name = input("What is your name?: ")
    Bid = int(input("What's your bid?: $ "))
    full = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    print("\n"*100)
    auction(Name,Bid)
winner = {}
money = 0
for key in bidders:
    if bidders[key] > money:
        winner = {}
        money = bidders[key]
        winner[key] = money
for key in winner:
    winner_name = key
print(f"The winner is {key} with a bid of ${money}")
