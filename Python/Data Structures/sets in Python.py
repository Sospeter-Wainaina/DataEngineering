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

#iterating through the set
for i in myset:
    print(i)
print(3 in myset) # returns true if the element exists in the set

#we can also use the union method to combine two sets and return a new set with all the items
evens = {2,4,6,8,10}
odds = {1,3,5,7,9}
primes = {2,3,5,7}

u = evens.union(odds)
print(u)

#we can also use the intersection method to return a new set with only the items that are present in both sets
i = evens.intersection(primes)
print(i)

#we can also use the difference method to return a new set with only the items that are present in the first set and not in the second set
d = evens.difference(primes)
print(d)

#we can also use the symmetric_difference method to return a new set with only the items that are present in one set and not in both sets
sd = evens.symmetric_difference(primes)
print(sd)
#we can also update a set with the items that are present in both sets
evens.update(odds)
print(evens)
#we can also use the intersection_update method to update a set with the items that are present in both sets
evens.intersection_update(primes)
print(evens)

#we can also use the difference_update method to update a set with the items that are present in the first set and not in the second set
evens.difference_update(primes)
print(evens)

#we can also use the symmetric_difference_update method to update a set with the items that are present in one set and not in both sets
evens.symmetric_difference_update(primes)
print(evens)