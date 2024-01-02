def make_class():
    class Hi:
        pass
    return Hi
print(make_class())

# Difference between a class and a meta class
# A class is an instance of a meta class. What this means is that a class is an object and an instance of a meta class.
# A meta class basically defines the rules for a class. It is the blueprint for a class.
# A class on the other hand defines a blueprint for an object.

# Lets create a class
class Meta(type):
    # we can define methods in a meta class
    # __new__ is a dunder method that is called before __init__
    def __new__(self,class_name,bases,attrs):
        print(attrs)
        a = {}

        for k,v in attrs.items():
            if k.startswith('__'):
                a[k] = v
            else:
                a[k.upper()] = v
        print(a)
        return type(class_name,bases,a)

class Dog(metaclass = Meta):
    x= 5
    y = 8
    def hello(self):
        print('Hi')

d = Dog()

d.HELLO()