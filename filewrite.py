# write to a file as easy as read 

f = open('newfilecreate.txt','w')

# f.write donot need to store in variable 
#it direct work on the file 
# Remeber to close the file after use it
#like f => fridge in your home


f.write('please write this letter to creatednewfile in text edi\
tor , you write it in vs code editor ')

# run it for first time it create newfile if not exist !!!
# run this code second time to update entire content with this 
# content 




f.close()
