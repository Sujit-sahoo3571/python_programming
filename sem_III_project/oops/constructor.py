class Employee :
    company = 'Google'
    def getSalary(self):
        print(f'Employee of this company {self.company} is {self.salary}')

#  def __init__ is default construct with arg self 
# constructor run when object created 
    def __init__(self):
        print('Employee is created ! ')

# object created 
sujit = Employee()
sujit.salary = 200 
sujit.getSalary()
