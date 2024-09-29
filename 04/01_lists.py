# LIST

letters = ["a", "a", "b", "c"] # we can store duplicates
mixed_type_list = ["a", 123, 123.5, None, False] # we can store multiple data types 
letters2 = list() #list konstruktor
letters2 = [] 
numbers = list(range(5))
print(numbers)

#indexing

name = "Sarah"
names = ["Sarah", "Tim", "Jimmy"]
print(names[:2]) #same indexing logic as we learned with strings

#changing items / elemek változtatása

names[0] = "Steve"
print(names)

names[:2] = ["Maria", "Dexter"]
print(names)

#inserting more
names[1:2] = ["Timmy", "Kyle"]
print(names)

#inserting less
names[1:3] = ["Jeremy"]
print(names)


#methods

#adding items
names.append("AddedRandomName")
print(names)

#names.append(["AddedRandomName", "AddedRandomName2"])
#print(names)

names.extend(["AddedRandomName", "AddedRandomName2"])
print(names)

#inserting to specified index
names.insert(0, "This is the first name")
print(names)

#deleting items from the list

#deleting specified item from the list:

names.remove("AddedRandomName")
print(names)

#deleting specified index:

names.pop(1)
print(names)

del names[1]
print(names)

names.clear()
print(names)


# asking the user for 3 favourite chocolates and print it out

chocolates = input("Give me your 3 favourite chocolates separated by a comma: ")
print(chocolates)
print(type(chocolates))
chocolate_list = chocolates.split(",")
print(chocolate_list)
chocolate_list.append("bounty")
print(chocolate_list)

#size of list
print(len(chocolate_list))
