def sumrecursive(num):
    if num == 1 :
        return 1
    elif num == 0 :
        return 0
    else :
        return num + sumrecursive(num-1)

val = int (input("Enter a Number "))

print(f'sum of n natural number is {sumrecursive(val)}')