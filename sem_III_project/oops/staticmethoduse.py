# sometimes we donot need to take self as default argument 
#static method we use 
class Employee :
    company = 'Google'
    def getSalary(self):
        print(f'Employee of this company {self.company} is {self.salary}')

    @staticmethod
    def greet():
        print('Good morining sir ')




sujit = Employee()
sujit.salary = 200000
sujit.getSalary() # Employee.getSalary(sujit)
# sujit.greet()  # Employee.greet(sujit)   
sujit.greet() 

        