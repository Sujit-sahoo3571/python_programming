with open('another.txt','r') as f :
    a = f.read()
if 'new' in a :
    print('new is present in text ')
else:
    print('new is not present in text ')