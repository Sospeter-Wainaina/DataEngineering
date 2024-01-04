# Sets are an unordered collection of items which only allow unique items
# Sets are mutable meaning we can change them

myset = {1,2,3,2,3,4,5,6,7,8,9,10}
print(myset) # only prints unique items
print(type(myset))

myset2 = set("Hello")
print(myset2)

#adding items to a set
myset.add(11)
myset.add(12)
print(myset)

#removing items from a set
myset.remove(12)
print(myset)
# myset.remove(12)# this will throw a Key error since 12 is not in the set

#we can also use the discard method, difference comes in when we try to remove an item that is not in the set discard will not throw an error
myset.discard(11)
print(myset)

#we can also use the pop method to remove an item from a set
print(myset.pop())# this will remove the first item in the set
print(myset)