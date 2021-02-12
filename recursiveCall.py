#recursive call 

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial_recursive(n-1)

fact = int(input('Enter the Number for factorial value:  '))

f = factorial_recursive(fact)

print(f)