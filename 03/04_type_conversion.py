word_1 = "apples"
word_2 = "oranges"

#type(), isinstance()

print(type(word_1))
print(isinstance(word_1, str))

# type conversion / típus konverzió functions

age = "13"
age = int(age) + 1
print(age)

#user input
age = input("Please provide your age:")
age_in_days = int(age) * 365
print(age_in_days)

name = input("Please provide your name:")
name_multipled = name * 10
print(name_multipled)

#truthy-falsy értékek
print(bool(1))
print(bool(0))

print(bool(""))
print(bool("something"))

#egyéb típuskonverzióra használható függvények:
float()
str()
int()
bool()