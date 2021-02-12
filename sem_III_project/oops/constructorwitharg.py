class Employee :
    company = 'Google'
    
#  def __init__ is default construct with arg self 
# constructor run when object created 
    def __init__(self, name , salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print('Employee is created ! ')

    def detail(self):
        print(f'Employee name is {self.name}')
        print(f'Employee salary is {self.salary}')
        print(f'Employee subunit is {self.subunit}')

# object created 
sujit = Employee('sujit',300,'developer')

# sujit = Employee() Error  missing 3 required positional arguments

sujit.detail()

