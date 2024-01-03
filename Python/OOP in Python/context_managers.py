# these two pieces of code are equivalent

file  = open('sile.txt',"a")
try:
    file.write("Hello World")
finally:
    file.close()

# This is equivalent to the following code which is a context manager. It is better because it automatically closes the file for us

with open("sample.txt","a") as file:
    file.write("Hello World")

class File:
    def __init__(self,file,method):
        self.file = open(file,method)

    # def __enter__(self): # this is the enter method which is called when we enter the context e.g. when we use the with statement "with open("sample.txt","a") as file:"
    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self,type,value,traceback):
        print(f"{type},{value},{traceback}")
        print("Exit")
        self.file.close()
        return True

with File('./sample.txt','w') as c:
    print("Middle")
    c.write("Hello")
    raise Exception()

# creating context managers using generators

from contextlib import contextmanager
@contextmanager
def file(filename,method):
    print("Enter")
    file = open(filename,method)
    yield file
    file.close
    print("Exit")

with file("test.txt","w") as f:
    print("Middle")
    f.write("Hello World")
