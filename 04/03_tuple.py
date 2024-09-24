#TUPLE

coordinates = (13.131231, 15.4321312)
print(coordinates[0])
print(coordinates[1])

#from an indexing perspective tuples are the same as the lists
print(coordinates[-1])
print(coordinates[1:2])
print(type(coordinates[1:2]))

print(coordinates.count(15.4321312))
coordinates.index(15.4321312)

coordinates[1] = 123


