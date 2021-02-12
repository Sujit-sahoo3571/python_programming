while True:
    
    print('Enter q to Quit ')
    i = input('Enter a Number :  ')
    if (i == 'q'):
        break

    try:
        num = int(i)
        if num > 45:
            print( ' Number Is Greater Than 45 ')
        else:
            print ('Number is less than 45 ')
    
    except Exception as e :
        print('Enter only Number ')
        print ('Error ',e)
