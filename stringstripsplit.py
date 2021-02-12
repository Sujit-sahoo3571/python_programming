
# strip remove spaces from beginning and ending of the sentences

mystring = input('Enter a string \n')
word = input('Enter the  word  : \n ')
if(word in mystring):
    mystring = mystring.replace(word,'')
    # mystring = mystring.strip()
    print(mystring.strip(), 'Removed string ')

else:
    print('Word not in the string ')

l = list(mystring.split())
for i in l :
    if i == ',':
        continue
    print(i, 'split string ')