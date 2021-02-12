#multiplication value print

num = int(input('Enter a Number :  '))

newlist = [num*i for i in range(1,11)]

print(newlist)

with open ('MulStoreFile.txt','a' ) as f:
    f.write(str(newlist))
    f.write('\n')
    print('Success')