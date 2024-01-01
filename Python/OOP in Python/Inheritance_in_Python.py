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

#Now we can create instances of the class Emp
employee_1 = Emp('Sospeter','Wainaina',120000)
employee_2 = Emp('Alice','Nungari',50000)
