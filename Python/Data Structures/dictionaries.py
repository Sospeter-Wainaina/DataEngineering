# Dictionaries are unordered mappings for storing objects. Previously we saw how lists store objects in an ordered sequence, dictionaries use a key-value pairing instead.

# This key-value pair allows users to quickly grab objects without needing to know an index location.
mydct = {"name":"John","age":23,"city":"Nairobi"}
print(mydct)
mydict2 = dict(name="Mary",age=27,city="Nairobi")
print(mydict2)

# they are mutable meaning we can change them
mydict2["email"] = "Mary@xyz.com"
print(mydict2)

# deleting an item from a dictionary
del mydict2["name"]
print(mydict2)

#altrnatively we can use the pop method
mydict2.pop("age")
print(mydict2)

# looping in a dictionary

for key in mydict2:
    print(key)

for k,v in mydict2.items():
    print(k,v)

# copying a dictionary is similar to copying a list
mydict3 = mydict2.copy()
print(mydict3)

# we can also merge two dictionaries
mydict4 = {**mydict2,**mydict3}
print(mydict4)
