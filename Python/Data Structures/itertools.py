# itertools is a module that implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML.
# Each has been recast in a form suitable for Python.

from itertools import product, permutations

#product computes the cartesian product of input iterables  (https://en.wikipedia.org/wiki/Cartesian_product)
a= [1,2]
b = [3,4]
prod = product(a,b,repeat=2)
print(list(prod))

# permutations are all possible orderings of a given collection of items
a = [1,2,3]
perm = permutations(a)
print(list(perm))