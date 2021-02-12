# relational > ,< ,<= ,>=, ==

# logical and ,or ,not
val = int(input('Enter a Number :  ')) 
if (val >18 and val < 56):
    print('You can work with us ')
elif(val > 100):
    print('You are too old ')
else:
    print('You can not work with us ')

mr = True 
if not mr:
    print('You are Miss. ')
else:
    print('You are Mr.') 
# is , in 
a = None
print(a is None) # true

l = [44,4 , 22,13,12 , 13,14,16,14,15]
print(44 in l) # True
print(45 in l ) #False