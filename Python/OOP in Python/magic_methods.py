class Emp:

    #class variables are variables that are shared among all instances of a class
    raise_amount = float(1.04)
    num_of_emps = 0
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@company.com"
        Emp.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = float(self.pay * self.raise_amount)

    # By default, all methods take the instance as the first argument. To change this, we use the @classmethod decorator so that the method takes the class as the first argument
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = float(amount)

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    #static methods do not pass anything automatically. They behave just like regular functions but we include them in our classes because they have some logical connection to the class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return f"Emp('{self.first}','{self.last}',{self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self,other):
        return self.pay + other.pay

# employee_1 = Emp('Sospeter','Wainaina',120000)
# employee_2 = Emp('Alice','Nungari',50000)
# print(employee_1.email)
# print(employee_2.email)
# print(employee_1.__repr__())
# print(employee_1+employee_2)

# lets define two lists
x = [1,2,3]
y = [4,5]
# You will see that when we add them together it will concatenate them
print(x+y)

#same with strings
print('a'+'b')

#for integers it behaves differently because it adds them together
print(1+2)

class Person:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Person('{self.name}')"

    def __mul__(self,other):
        if type(other) is not int:
            raise TypeError('Can only multiply by integers')
        return self.name * other

    def __len__(self):
        return len(self.name)
p1 = Person('Sospeter')
# when we print p1, we get the location of the object in memory
# This is because we have not defined a __repr__ or __str__ method
# which tells python how to print the object
print(p1)
print(p1*3)
print(len(p1))