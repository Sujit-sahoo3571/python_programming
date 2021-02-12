# Enter eight number and print unique values
# set operation 
a = input ('Enter a Number ')
b = input ('Enter a Number ')
c = input ('Enter a Number ')
d = input ('Enter a Number ')
e = input ('Enter a Number ')
f = input ('Enter a Number ')
g = input ('Enter a Number ')
h = input ('Enter a Number ')
i = input ('Enter a Number ')
# s = set()
s = {a,b,c,d,e,f,g,h,i}
# s.add(a)
# s.add(b)
# s.add(c)
# s.add(d)
# s.add(e)
# s.add(f)
# s.add(g)
# s.add(h)
# s.add(i)
print(s)
# having 4 element in set 
# it print 3 element with len = 3
# as 18 and 18.0 is same in python smart enough right !

newset = {18,'18',18.0,18.1}
print(newset)
print(len(newset))

# difference in empty set and empty dict 
# set = set() , dict = {}
d = {}
ns = set()
print('dict ', type(d),' set ', type(ns))