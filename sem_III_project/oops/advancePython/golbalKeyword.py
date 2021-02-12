# global keyword 
a = 100

def whatYouPrint():
    # a = 19
    # print('I am in function ', a) 
    # #Error as you can not use it before 
    # if you are using in same function global then it forbid to use
    # first 
   
    global a 
    a = 78
    print('I am in function ', a)


print('a = ',a)
whatYouPrint()
# print the changes of global value (scope outside of all the variable)
print('a = ',a)