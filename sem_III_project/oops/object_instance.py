class Employee:
    company = 'Google'

# creating object instanciation 
sujit = Employee()
swagatika = Employee()

# object attribute assign 
sujit.salary = 334543

#  attribute that belongs to object 
print(sujit.salary)

# class attribute
class Employee1:
    company = 'Google'
    salary = 34333
s = Employee1()

print(s.salary)

s.salary = 45443

print(s.salary)
# it first looking for object attribute assign
# then check for class attribute if not found 

s.age = 34

print(s.age)
# throws an error as it is not specified 
# print(s.address) 
