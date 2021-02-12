# use Finally here 
try:
    val = int(input('Enter a Number '))
    a = 1/val

except Exception as e :
    print(e)
    exit()
finally:
    print('We are Done! ')
    

