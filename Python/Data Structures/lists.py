# Lists are mutable, ordered, and allow duplicate elements
#they are a collection of items in a particular order
mylist = ["banana", "cherry", "apple"]
print(mylist)
#we can create an empty list and later come to append items to it like so
mylist2 = list()
print(mylist2)
#They accept items of different data types
mylist3  =  [5,"apple",True,5.6]
print(mylist3)
#accessing elements in the list we use the index with 0 being the first element
item = mylist[0]
print(item)
#accessing elements with a negative index starts from the end of the list
item = mylist[-2] #this will print banana
#accessing an index that is out of range will throw an error of index out of range
#we can also loop through the list

for i in mylist:
    print(i)

#we can also check if an item is in the list

if "banana" in mylist:
    print("yes")
else:
    print("no")

print("banana" in mylist)

#we can also check the length iof the list
print(len(mylist))
#add items to a list we use append method which ill add an item to the end of the list
mylist.append("orange")
print(mylist)

# we cn also insert an item at a soecific index
mylist.insert(2,"lemon")
print(mylist)

#we can also remove items from a list
mylist.pop() #this will remove the last item in the list
print(mylist)

#we can also remove an item at a specific index
mylist.remove("lemon")
print(mylist)

# we can clear all the elements in a list using the clear method
# mylist.clear()
# print(mylist)

# we can alsosort a list like so

mylist5 = [5,3,7,8,-3,1,-7,1,3,6]
mylist5.sort()
print(mylist5)



