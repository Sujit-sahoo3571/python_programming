# tuple specified with ()
t1 = () # empty tuple
t2 = (1) # wrong way of declare the tuple 

t3 = (1,) # right way of declaring the tuple with one element

t4 = (44,55,88.77,66,44,55,44,56,44,656)  # its ok  t4 = (44,55,88.77,66,)  
# printing tuples
# tuples are immutable (no mutation (change)) you cant change
#elements !

# t4[0] = 56 Error ! 
print(t1,t2,t3,t4)

# count the occurance of element in tuple 

c1 = t4.count(44)
print(c1)

# index value of the element in the tuple found first

c2 = t4.index(56)
print(c2)


