# lambda is a simple one line expression anonymous function often used as an inline function
# syntax: lambda arguments: expression

add10 = lambda x: x+10
print(add10(89))

mult = lambda x,y:x**y
print(mult(2,3))

dlist = [(1,2),(15,4),(9,6),(7,8)]
dlist_sorted = sorted(dlist, key = lambda x:x[1])
print(dlist)
print(dlist_sorted)