import random
score = 0
game_continue=True
names_of_A = []
data = [
    
    {
        'name':'Instagram',
        'followers': 568,
        'description': 'Social media platform',
        'country':'United States'},
    {
        'name':'Ronaldo',
        'followers': 665,
        'description': 'Footballer',
        'country':'Portugal'
    },
    {
        'name':'Ariana Grande',
        'followers': 183,
        'description': 'Musician',
        'country':'United States'
    },
    {
        'name':'The Rock',
        'followers': 181,
        'description': 'Wrestler',
        'country':'United States'
    },
    {
        'name':'Virat Kohli',
        'followers': 689,
        'description': 'Cricketer',
        'country':'India'
    },
    {
        'name': 'Amir Khan',
        'followers': 351,
        'description': 'Film Star',
        'country':'India'
    },
    {
        'name':'Narender Modi',
        'followers': 225,
        'description': 'Politician',
        'country':'India'
    },
    {
        'name':'Rudraksh Sharma',
        'followers': 82,
        'description': 'Engineer',
        'country':'Dubia'
    },
    {
        'name':'Cillian Murphy',
        'followers': 1000,
        'description': 'Movie Star',
        'country':'Irish'
    },
    {
        'name':'Christian Bale',
        'followers': 999,
        'description': 'Movie Star',
        'country':'United States'

    },
    {
        'name':'Brad Pitt',
        'followers': 867,
        'description': 'Movie Star',
        'country':'United States'
    },
    {
        'name':'Tom Hardy',
        'followers': 900,
        'description': 'Movie Star',
        'country':'British'
    }
]
def start_game():
    #Selecting people
    global score, game_continue,names_of_A
    people = random.sample(data, k=2)
    #Person A
    if score == 0:
        A = people[0]
    else:
        A = names_of_A[-1]
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    #Person B
    B = people[1]
    names_of_A.append(people[1])
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
    choice=input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == 'a':
        if A['followers'] > B['followers']:
            score += 1
            print(f"You are right! Current score: {score}")
        else:
            print("You are wrong.\nGAME OVER")
            game_continue = False
    elif choice == 'b':
        if B['followers'] > A['followers']:
            score +=1
            print(f"You are right! Current score: {score}")
        else:
            print("You are wrong.\nGAME OVER")
            game_continue = False
    else:
        print("You have entered wrong input.\nGOOD BYE")
        game_continue = False
#continue game
while game_continue:
    print('''

  ___ ___ .__       .__                   .____                               
 /   |   \|__| ____ |  |__   ___________  |    |    ______  _  __ ___________ 
/    ~    \  |/ ___\|  |  \_/ __ \_  __ \ |    |   /  _ \ \/ \/ // __ \_  __ \
\    Y    /  / /_/  >   Y  \  ___/|  | \/ |    |__(  <_> )     /\  ___/|  | \/
 \___|_  /|__\___  /|___|  /\___  >__|    |_______ \____/ \/\_/  \___  >__|   
       \/   /_____/      \/     \/                \/                 \/    
          
          
          ''')
    start_game()
