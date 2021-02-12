class Employee :
    company = 'Google'
    def getSalary(self):
        print(f'Employee of this company {self.company} is {self.salary}')

sujit = Employee()
sujit.salary = 200000
sujit.getSalary() # Employee.getSalary(sujit)
        
        
        