# create an empty dict 
# add user input 
# print the faviourite language of your friend 

# empty dict 
mydict = {}

# 6 input from user 

a = input('Enter your favourite Language subrat ')
b = input('Enter your favourite Language sujit')
c = input('Enter your favourite Language naresh  ')
d = input('Enter your favourite Language judhistir ')
e = input('Enter your favourite Language happy')
f = input('Enter your favourite Language Rashmi ')


# assign the value 
#can direct assign using index method
mydict['subrat'] = a
mydict['sujit'] = b
mydict['naresh'] = c
mydict['judhi'] = d
mydict['happy'] = e
mydict['rashmi'] = f

# when two keys name is same
mydict['happy'] = a 

# printing the value 
print(mydict.keys())
print(mydict.values())
print(mydict)
# Note input return string always
# Note two keys cannot be same else it will replace the last value
# Note two values can be same 

# Note set contain unique and immutable value
# set can not contain list 
# so set value can not be changed 
# e.g  s = {1,3,5,'auto',[2,3]} throw an error
#  unhashable type: 'list'
# s = {1,3,5,'auto',(2,3)} tuple can not modified .



