a = int(input('Enter 1st Number :  '))
b = int(input('Enter 2st Number :  '))
c = int(input('Enter 3st Number :  '))

if (a > b and a >c ):
    print(f'The greatest Number is {a} ')
elif (b > c and b > a ):
    print(f'The greatest Number is {b} ')
else:
    print(f'The greatest Number is {c} ')