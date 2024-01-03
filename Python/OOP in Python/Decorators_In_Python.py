# Decorators changes the behaviour of a function without having to change the code of the function itself.

def func(f):
    def wrapper():
        print("Started")
        f()
        print("Ended")
    return wrapper

# def func2():
#     print("I am function2")
#
# x = func(func2)
# print(x)
# x()

def func(x):
    def wrapper(*args,**kwargs):
        print("Started")
        rv = x(*args,**kwargs)
        print("Ended")
        return rv
    return wrapper
@func
def func3():
    print("I am function3")
func3()
@func
def func4(y=None,x=None):
    print("This function carries the following value/s",y,x)
    return x

print(func4([10,11,12],3))

# We can also use decorators to time functions
import time

def timer(f):
    def wrapper(*args,**kwargs):
        start = time.time()
        print("Started")
        rv = f(*args,**kwargs)
        time_taken = time.time() - start
        print(f"Time taken is {time_taken}")
        return rv
    return wrapper
@timer
def calc1(b):
    for _ in range(b):
        x = b**b
    return x
calc1(10000)