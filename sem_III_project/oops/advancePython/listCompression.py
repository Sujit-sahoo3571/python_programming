# list compression 
listNumber1 = [77,8,3,2,11,34,335,56,32,67,76,89,70,67.76,77]

# for i in listNumber1:
#     if i % 2 ==0:
#         print(i)

list2 = [ i for i in listNumber1 if i%2 ==0 ]

print(list2)

# print the set 
set1 = { i for i in listNumber1 if i>30}
print('set is ',set1)
print(type(set1), ' ', type(list2))