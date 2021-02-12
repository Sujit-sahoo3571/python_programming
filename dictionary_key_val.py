# A dictionary take a list , a string , another dict, int
d = {
    "sujit":3545321,
    'king': 'How are you sujit !!! ',
    'list': [4,5,3,2,1,2,3,4,5],
    'book' : {'cool': 'this is awsome '},
    44: 879
}

# print(d)
# print(d['sujit'])
# print(d['king'])
# print(d['list'])
# print(d['book'])
# print(d['book']['cool'])
# stored unordered 
# mutable 
# d['list'] = [45,33,66]
# print(d['list'])
#stored as key based 
# no duplicate value pair exist
#it over ride if you want to store duplicate value
#it takes integer as the key 

# print(d.keys())
# print(d[44])
# print(type(d.keys()))
# print(list(d.keys()))

# update newDict here 
newDict = {445: 553,
'human': 77,
'animal': 49,
'extraordinary' : 7.4

}


# get , value, update method



print(d.values())
d.update(newDict)
print(d['human'])
print(d.get('animal'))
print(d.get('beast')) # return None as no entry exist

print(d['animal'])
# print(d['beast']) # return Error

# print(d)
