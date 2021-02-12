#readline read 1 line at a time

# first line
f = open('myname.txt') # read file once !

text = f.readline() # readline read first line of text

print(text)
# second line 

text = f.readline() # readline read first line of text

print(text)
# Third line 

text = f.readline() # readline read first line of text

print(text)
f.close()

# file operation on 
# read => r
# write => w
# append => a
# updating => +
# read binary text = > rb 
# read text file = > rt

# read a binary file let's see 

f = open('lady.jpg','rb')

text = f.read(19) # f.read() crash the program as a 
# lot of numbers 

print(text)

f.close()