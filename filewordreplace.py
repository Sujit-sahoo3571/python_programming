# open a file put your word in it and make changes in words you
# want to change 

yourword = input('Enter some text here ')


with open('another.txt','w') as f: 
    f.write(yourword)

word = []

n = int(input('How many word to select ? '))
for i in range(n):
    w = input('Enter a word ')
    word.append(w)

with open('another.txt','r') as f :
    text = f.read()

print(word)
# print(text)
for w in word:
    if w in text : 
        text = text.replace(w ,'@$%$%^')
        with open('another.txt','w') as f:
            f.write(text)

print(text)
# print('Done ! ')



# print(word)
