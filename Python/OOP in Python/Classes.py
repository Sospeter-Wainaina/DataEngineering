#Say we had an app for our company and we wanted to create a class for our employees
# We can create a Class named Employee and then create instances fo that class.

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

#print instances
print(emp_1)
print(emp_2)
#instance variables These are unique to each instance and this is where we pass them manually
emp_1.first = 'Sospeter'
emp_1.last =  'Wainaina'
emp_1.email = 'Sospeter.Wainaina@gmail.com'
emp_1.pay = 120000

emp_2.first = 'Alice'
emp_2.last =  'Nungari'
emp_2.email = 'Alice.Nungari@gmail.com'
emp_2.pay = 50000

print(emp_1.email)
print(emp_2.email)

#This is a lot of work and we can use a constructor to make it easier
# a constructor is a function that runs automatically when we create an instance of a class

class Emp:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

#Now we can create instances of the class Emp
employee_1 = Emp('Sospeter','Wainaina',120000)
employee_2 = Emp('Alice','Nungari',50000)
print(employee_1.email)
print(employee_2.email)
print(employee_1.fullname())