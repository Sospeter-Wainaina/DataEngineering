class Emp:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self,name):
        first, last = name.split('-')
        self.first = first
        self.last = last

employee_1 = Emp('Sospeter','Wainaina',120000)
employee_2 = Emp('Alice','Nungari',50000)
employee_1.first = 'Jim'
employee_1.last = 'Halpert'
print(employee_1.first)
print(employee_1.last)
print(employee_1.email)

employee_2.fullname = 'Emmanuel-Mukuri'
print(employee_2.first)
print(employee_2.last)
print(employee_2.email)