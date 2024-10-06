import time

#working with lists (same exact way of working for tuple, set, frozenset):
playlist = ["I'm a barbie girl", "8 óra munka", "Autó egy szerpentinen", "Heavy is the crown"]

for song in playlist:
    print(f"Playing {song}")
    #time.sleep(1)


print("-------------------")
#working with strings:
name = "Steve Jobs"
for char in name:
    print(char)

#working with dictionaries:

student = {
    "name": "John",
    "age": 20,
    "grades": [4, 5, 5],
    "major": "Computer Science",
    "is_active": True
}

#looping over both keys and values:
for k,v in student.items():
    print(f"Key: {k}, value: {v}")

#looping over keys only:
for k in student.keys():
    print(k)

#looping over values only:
for k in student.values():
    print(k)

#looping over a range:
for id in range(5):
    print(id)