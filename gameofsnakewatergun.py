# snake , water , gun

import random

choice = {1:'s', 2:'w', 3:'g'}

player = input('Enter snake(s), water(w), gun(g) :  ').lower()

ran = random.randint(1,3)

if player == choice[ran]:
    print('Match tie ')
    exit()
# print(ran)
# print(choice[ran])
if player == 's' and choice[ran] == 'w':
    player = False
elif player == 'w' and choice[ran] == 's':
    player = False
elif player == 'g'and choice[ran] == 'w':
    player = False
else :
    player = True

if player:
    print(f'You Win the match, computer enter {choice[ran] } ')
else : 
    print(f'You lose it , computer win the match computer enter {choice[ran] }')

