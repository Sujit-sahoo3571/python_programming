print('A Number for the division ')
try:
    a = int(input('Enter a Number '))
    c = 1/a
    print(f'Your 1/a =  {c } ')

except ValueError as e :
    print('Enter a Valid Value ')

except ZeroDivisionError as e :
    print('Infinte')

print('Thanks for using this software ! ')