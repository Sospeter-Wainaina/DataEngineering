from collections import Counter

a = "aaaaakbkkkbkvkjbiiiurgbkjbk"
print(Counter(a))

for k,v in Counter(a).items():
    if v == max(Counter(a).values()):
        print(f"{k} is the most popular item with {v} occurrences")
    # print(k,v)

b = [1,2,2,2,2,2,3,4,5,5,55,66,75,4,33,3,2,3,44,45,5,6,6]
print(Counter(b))