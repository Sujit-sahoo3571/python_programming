# reduce available in functools
# rolling computation on sequential elements

from functools import reduce

sum = lambda a,b : a+b
mul = lambda a,b : a*b

ls = [1,2,3,4]

print(reduce(sum,ls))
print(reduce(mul,ls))
