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

a = [1,2,3,4,5,6,7,8,9,10]
print([x**2 for x in a])

# the same can be achieved using map and lambda
# map applies a function to all the items in an input list

print(list(filter(lambda x:x%2==0,list(map(lambda x:x**2,a)))))

print([x for x in a if x%2==0])