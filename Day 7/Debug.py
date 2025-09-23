import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ["aardvark", "baboon", "camel"]
################################################
choosen_word = random.choice(word_list)
print(choosen_word)
dash = ""

for blank in range(len(choosen_word)):
    dash+="_"
print(dash)
##################################################
lives = 0
game_over = False
correct_letters =[]
previous_try =[]
while game_over == False and lives < 7:

    guess = input("Enter letter choosen by you: ").lower() 

    letter_match = ""
    
    for match in choosen_word:
        if match == guess:
            letter_match+= match
            correct_letters.append(match)
        elif match in correct_letters:
            letter_match += match
        else:
            letter_match+="_"
    print(letter_match)
    if letter_match in previous_try:
        print(HANGMANPICS[lives])
        lives+=1
    previous_try.append(letter_match)
    if "_" not in letter_match:
        game_over == True
if lives >= 7:
    print("You've lost all lives. YOU LOST.")
elif game_over == True:
    print("You've won the game. YOU WON.")
