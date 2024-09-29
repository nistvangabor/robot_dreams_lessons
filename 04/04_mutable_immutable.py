my_list = [1, 2, 3]
print("Original list ID:", id(my_list))  # Prints the ID of the list

my_list.append(4)  # Modify the list
print("Modified list ID:", id(my_list))  # ID remains the same
print("Modified list:", my_list)



my_tuple = (1, 2, 3)
print("Original tuple ID:", id(my_tuple))  # Prints the ID of the tuple

# Attempt to modify the tuple (will raise an error)
# my_tuple[0] = 4  # Uncommenting this will raise a TypeError

new_tuple = my_tuple + (4,)  # Create a new tuple
print("New tuple ID:", id(new_tuple))  # ID is different
print("Original tuple:", my_tuple)
print("New tuple:", new_tuple)

### strings are also immutable

name = "Sarah"
#name[0] = "T"
print(name)
name = f"T{name[1:]}"
print(name)

#mutable:
#lists, dictionaries, sets, (bytearrays)

#immutable: int, bool, float, string, tuple, frozenset, nonetype