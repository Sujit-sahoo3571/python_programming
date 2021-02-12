# creating class with attribute company that belongs to class 
class Employee:
    company = 'Google'


# instantiation  the object
sujit = Employee()
swagatika = Employee()

# print company attribute of class using distinct object 
print(sujit.company)
print(swagatika.company)

# change the class attribute here using classname.attribute =?

Employee.company = 'YouTube'

# printing after changing class attribute
print(sujit.company)
print(swagatika.company)
