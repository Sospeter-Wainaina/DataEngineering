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

class BusinessAnalyst(Emp):
    raise_amount = 1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Emp):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees == None:
            self.employees= []
        else:
            self.employees = employees

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for e in self.employees:
            print('-->',e.fullname())


#Now we can create instances of the class Emp
Ba_1 = BusinessAnalyst('Sospeter','Wainaina',120000,'SQL')
Ba_2 = BusinessAnalyst('Alice','Nungari',50000,'Python')
# print(employee_1.email)
# print(help(BusinessAnalyst))
# print(Ba_1.pay)
# Ba_1.apply_raise()
# print(Ba_1.pay)
# print(Ba_1.prog_lang)
# print(Ba_2.prog_lang)

mgr_1 = Manager('Everlyne','Sunguti',260000,[Ba_1])
print(mgr_1.email)
mgr_1.add_employee(Ba_2)
print(mgr_1.print_emps())