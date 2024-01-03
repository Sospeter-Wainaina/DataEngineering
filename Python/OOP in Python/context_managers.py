# these two pieces of code are equivalent

file  = open('sile.txt',"a")
try:
    file.write("Hello World")
finally:
    file.close()

# This is equivalent to the following code which is a context manager. It is better because it automatically closes the file for us

with open("sample.txt","a") as file:
    file.write("Hello World")

