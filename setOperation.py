#empty set 

b = set()
c  = {2,5,4,1}
print(b,c,type(b), type(c))
# Note { } - empty dictionary not a set 
d = {}
print(d, type(d))
# set adding element 
b.add(0)
b.add(5)
b.add(7)
print(b)
c.add((4,5,3,6))
print(c)
#set is unordered ,unindex,can not take list or dict data type
# as list or dict cannot be hashed
#list or dict are mutable 
# c.add([44,55,33,54])  #Error

# set methods add, remove,pop,union,intersect
print('Remove c pop c union c printing.....')
c.remove(5)
print(c)
print(c.pop())
print(c)
d = c.union({1,4,66,7}) # union operation return to another set
print(c, ' c  set ')
print(d, 'd set after modified return to a new set ')
e = c.intersection({0,4,5,2})
print(e)
# clear method make set empty
e.clear()
print(e)