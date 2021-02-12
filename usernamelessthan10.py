username = input('Enter a User Name ')
password = input('Enter a password ')

if len(username)<10  or len(password) <10:
    print('Enter a UserName length greater than 10')
elif '@' in username or '@' in password:
    print('Nice choice of UserName or Password')
else:
    print('your username and password is good')