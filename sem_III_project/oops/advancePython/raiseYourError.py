print('Custom Error Create and Handling ')

def Increment (num):
    try:
        return int(num)+1 

    except:
        raise ValueError('This is not Good - sujit ')


a = input('Enter a Number ')
print(Increment(a))




