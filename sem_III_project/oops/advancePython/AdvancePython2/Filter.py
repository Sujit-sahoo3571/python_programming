# filter (function , list )

def greater_than_5(x):
    if x > 5:
        return True
    else:
        return False

g10 = lambda x : x >10

ls = [1, 2, 3, 5,8,10, 4, 44, 33, 24, 23, 53, 234]

print(list(filter(greater_than_5, ls)))
print(list(filter(g10, ls)))
