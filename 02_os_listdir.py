import os
arr = os.listdir() #this line give you list of dir present 
# in current directory
a = 'Design'
b = ''' cool man
i  am in 
another 
world !!! '''
c = 56554
d = 54.67
e = True 
# printing value 
f = None
print (a, b, c, d, e )

# printing types 

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f),  f )

# assignment operator 

a = 56
b = 64
print ( " sum ", a+b )
print ( 'sub ', a-b , 'mul ' , a*b )
print (' div ', a/b , 'div int ', a//b )

# # print ('assign ', a += b)
# print ('assign ', a -= b)
print ('reminder  ', b %a)
# print ('assign ', a /= b)
# print ('assign ', a //= b) Error 
a = input ('Enter a number ')
print( a , type(a))
a = int(a)
print(a, type (a) )
print(arr)