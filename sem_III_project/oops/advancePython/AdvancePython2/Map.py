# map 
l = [1,3,5]

squar = lambda x : x*x

# l2 = []

# for i in l:
#     l2.append(squar(i))

# print(l2)

# method 2 
# map(function , input-list) then typecast it to list 
#  list(map(function , input-list))

print (list(map(squar,l)) )
