# a = input('Enter a Number a = ')
# b = input('Enter a Number b = ')

# a = int(a)
# b = int(b)
# print( 'average of Numbers = ', float ((a+b) /2) )

name = 'sujit'
# l = len(name)
# print(l ,name, name[0])
# name[1] = 'a' # str does not support item assignment 
# print(l ,name, name[0])
# print ( name[-5])
# print (name[-1:]) # iterate forward 
# print ( name[-2])

# skip no of word or print that no of word 

# name = 'SujitiscoolmanHelloworld@'
# l = len(name)
# d = name[::2]  # 0:l:2 or print every 2 nd word 
# print(d, l)

# d = name[3:10:1]  # 3:10:1 or print every 1 st letter no skip 
# print(d, l)

# name = input('Enter your name  ')
# print ('Good after Noon !  '+ name )
# print ('find string/ word ', name.find('s'))
# print ('replce word / string ', name.replace('sujit','mam^2'))
# print('capitalize ', name.capitalize())


# customize replace the letter template 

# letter = ''' Hi ! <|NAME|>,
#     nice to meet you 
#     this is an  official 
#     letter for the meeting 
#     on date - <|DATE|> 
#     thank you 
#     sujit ....
#     '''
# name = input('Enter your name \n')
# date = input('Enter the date  \n ')

#     #**** 

# letter = letter.replace('<|NAME|>',name)
# letter = letter.replace('<|DATE|>',date)

# print(letter)

# # find the double space
# letter = 'this is a double  space sentence '
# print(letter.find('  '))

# List 
c = ['sujit ', 'swagatika', 'anwesha','silpa', 'varati ']
print(c)
#slicing list 
print(c[0:4])

# for loop iteration
for i in c:
    print(i)
