items = ['apple', 'banana', 'cherry', 'date']
threshold = 3

length = len(items)
if length > threshold:
    print(f"The list has {length} items, which is greater than {threshold}.")

# ugyanez a walrus operátorral:

if (length := len(items)) > threshold:
    print(f"The list has {length} items, which is greater than {threshold}.")