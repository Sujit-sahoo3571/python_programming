# open and check if python present or not 

with open('logbook.txt','r') as f:
    text = f.read()
if 'python' in text.lower() :
    print('python is present ')
else :
    print('python not present ')

# check for line number it is present 
i = 1 
text = True
with open('logbook.txt', 'r') as f:
    while text :
        text = f.readline()
        if 'python' in text :
            print(i)
        i += 1 # yes it working assignment !!!
