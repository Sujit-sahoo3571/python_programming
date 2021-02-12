# create a dictionary
mydict = {
    'waqt': 'time',
    'intezar':'wait for someone',
    'kahani': 'story',
    'itafaq' : 'by chance'
}
print('-------',mydict.keys(),'--------\n' )

w = input('Enter a Hindi word : \n')
print('\n',mydict.get(w))
