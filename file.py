# open read and close a  file 

# f = open('myname.txt','r')


f = open('myname.txt')  # by default it is in read mode 

data = f.read() # give all the character present in file 

# data = f.read(5) # it read first 5 character from the file 

print(data)

f.close()


# file operation on 
# read => r
# write => w
# append => a
# updating => +
# read binary text = > rb 
# read text file = > rt