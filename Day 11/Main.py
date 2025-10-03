#If you get stuck then remember family.
import random
Begin = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ")
round = 0
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user = []
computer = []
while Begin == 'y':
    def card_alot():
        if round == 0:
            user.extend(random.choices(cards,k=2))
            computer.extend(random.choices(cards,k=2))
        else:
            if sum(user) < 21:
                num1 = random.choice(cards)
                if num1 == 11:
                    if num1 + sum(user) > 21:
                        user.append(1)
                    else:
                        user.append(11)
                else:
                    user.append(num1)
            if sum(computer) < 21:
                num2 = random.choice(cards)
                if num2 == 11:
                    if num2 + sum(computer) > 21:
                        computer.append(1)
                    else:
                        computer.append(11)
                else:
                    computer.append(num2)
        return f"Your cards: {user}, current score: {sum(user)}\nComputer's first card: {computer[0]}"
    if round == 0:    
        print(card_alot())
    def result():
            if sum(user)>21:
                return 'You went over. You lose'
            elif sum(user)>sum(computer):
                return f"Your final hand: {user}, final score: {sum(user)}\nComputer's final card: {computer}, final score:{sum(computer)}\nYou Won."
            elif sum(user)==sum(computer):
                return f"Your final hand: {user}, final score: {sum(user)}\nComputer's final card: {computer}, final score:{sum(computer)}\nIt's a draw."
            else:
                return f"Your final hand: {user}, final score: {sum(user)}\nComputer's final card: {computer}, final score:{sum(computer)}\nYou lose"
    if sum(user) < 21:
        next_move =input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if next_move == 'y':
            round+=1
            card_alot()
    if sum(user) == 21 or next_move == 'n' or sum(user) > 21:
        print(result())
        Begin="n"
