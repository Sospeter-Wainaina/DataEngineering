from collections import Counter, namedtuple

a = "aaaaakbkkkbkvkjbiiiurgbkjbk"
print(Counter(a))

for k,v in Counter(a).items():
    if v == max(Counter(a).values()):
        print(f"{k} is the most popular item with {v} occurrences")
    # print(k,v)

# print(Counter(a).most_common(1))
# print(Counter(a).most_common(1)[0][0]) # this will print the most common item in the string a

Person = namedtuple(field_names = ['name','age','city'],typename='Person')

p1  = Person('Sospeter',23,'Kiambu')
print(p1)
print(p1.name)
print(p1.age)
print(p1.city)