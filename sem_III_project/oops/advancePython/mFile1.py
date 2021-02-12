# using __name__ == '__main__'

def greet(name):
    print(f'Good Morning , {name}')


print(__name__)
if __name__ == "__main__":
    name = input('Enter Your Name ')
    greet(name)