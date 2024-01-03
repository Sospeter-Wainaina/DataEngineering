# Generators in Python
# Generators are iterators. They are a special type of function that will generate information and not store it in memory.
# They will only generate the information when it is needed.

class Gen:
    def __init__(self,n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()
        rv = self.last**2
        self.last += 1
        return rv

# g = Gen(100000000)
#
# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break

# Now lets convert the above class to a generator


def generator_function(n):
    for i in range(n):
        yield i**2

g = generator_function(1000)

for i in g:
    print(i)

