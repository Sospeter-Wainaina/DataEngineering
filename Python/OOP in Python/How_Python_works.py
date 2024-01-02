# Python is compiled then interpreted.
# The compiler takes in the high level code and converts it into byte code.
# The byte code is then interpreted by the interpreter.
# Python will notice the error at runtime. and not compile time. take for instance the following code:

class Dog:
    def __init__(self,name):
        #we call a method that does not exist
        # You will get an error at runtime
        self.name = name
        self.bark()

#You notice when it is compiled, there is no error. It is only at runtime that you get the error.
# When we create an instance of the class, the __init__ method is called and the error is raised.
dog_1 = Dog('Fido')