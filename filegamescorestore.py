with open('gamescore.txt','r') as f :
    a = f.read()

def game():
    score = int(input('Enter your score :  '))
    return score

score = game()

if a == '':
    with open('gamescore.txt','w') as f :
       f.write(str(score))

elif score > int(a) :
    with open('gamescore.txt','w') as f :
        f.write(str(score))
else :
    print('Your score is not beat yet !!! ')




