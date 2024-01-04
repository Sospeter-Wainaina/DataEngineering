# tuples are similar to lists only that tuples cannot be changed meaning they are immutable
# we use () to create a tuple
my_tuple = ("banana","apple","mango")
print(my_tuple)

#we can also create tuples using the inbuilt tuple function
my_tuple2 = tuple(["banana","apple","mango"])
# print(my_tuple2)
print(type(my_tuple2))

#tuples ae immutable meaning we cannot change them
# my_tuple2[0] = "orange" will throw an error

#accessing items in a tuple is similar to accessing items in a list
item = my_tuple[0]
print(item)

#getting the length of a tuple
print(len(my_tuple))

my_tupple3 = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n")
#getting the index of an item
print(my_tupple3.index("a"))# its at the 0th index
#counting the number of times an item appears in a tuple
print(my_tupple3.count("a"))# it appears once
#converting a tuple to a list
my_list = list(my_tupple3)
print(my_list)
print(type(my_list))

# When creating a tuple with only one item we need to add a comma after the item otherwise it will be considered as a string
my_tuple4 = ("banana")
print(type(my_tuple4))# this will be a string
my_tuple5 = ("banana",)
print(type(my_tuple5))# this will be a tuple

#slicing in tuples
print(my_tupple3[2:5])
print(my_tupple3[::2])# this will print every second item
print(my_tupple3[::-1])# this will reverse the tuple

# we cna also unpack a tuple tuple
x,y,z = (1,2,3)
print(x)
print(y)
print(z)

a,b,*c,d = (1,2,3,4,5,6,7,8,9)
print(a)
print(b)
print(c)
print(d)

