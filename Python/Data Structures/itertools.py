# itertools is a module that implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML.
# Each has been recast in a form suitable for Python.

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle
import operator
#product computes the cartesian product of input iterables  (https://en.wikipedia.org/wiki/Cartesian_product)
a= [1,2]
b = [3,4]
prod = product(a,b,repeat=2)
print(list(prod))

# permutations are all possible orderings of a given collection of items
a = [1,2,3]
perm = permutations(a,2)
print(list(perm))

# combinations are all possible combinations of a given collection of items
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))

# combinations with replacement are all possible combinations of a given collection of items with replacement
a = [1,2,3,4]
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

# accumulate returns accumulated sums or accumulated results of other binary functions
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))

# we can also use a different operator other than sum
a = [1,2,3,4]
acc = accumulate(a, func=max)
print(a)
print(list(acc))

# groupby groups the items in an iterable

a= [1,2,3,4,5,6,7,8,9,10]
# def smaller_than_5(x):
#     return x<5

group_obj = groupby(a, key=lambda x:x<5)
for key,value in group_obj:
    print(key,list(value))

persons = [{'name':'Tim','age':25},{'name':'Dan','age':25},{'name':'Lisa','age':27},{'name':'Claire','age':28}]
groupobj = groupby(persons, key = lambda x:x['age'])
for k,v in groupobj:
    print(k,list(v))

#couunt function starts at tehe given interger and adds one infinitely

for i in count(10):
    print(i)
    if i == 15:
        break