# itertools is a module that implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML.
# Each has been recast in a form suitable for Python.

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
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
def smaller_than_5(x):
    return x<5

group_obj = groupby(a, key=smaller_than_5)
for key,value in group_obj:
    print(key,list(value))