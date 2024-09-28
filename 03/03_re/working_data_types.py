import math
#functions

#function != method

#len()

word_1 = "apple"
word_2 = "banana"

print(len(word_2))

sum_word_length = len(word_1) + len(word_2)
print(sum_word_length)

#type(), isinstance()

print(type(word_1))
print(isinstance(word_1, str))

#type conversion / típus konverzió

age = "13"
age = int(age) + 1
print(age)

#egyéb típuskonverziós function-ök:
#bool(), str(), int(), float()
print(bool(1))
print(bool(0))

#concatenation
first_name = "Tim"
last_name = "Johnson"
full_name = first_name + " " + last_name
print(full_name)
sentence = "Hi! My name is " + first_name + " " + last_name + "."
print(sentence)

#interpolated string / f-string

sentence = f"Hi! My name is {first_name} {last_name}."
print(sentence)


#string slicing
#indexelhetőség

fruit = "raspberry"
print(fruit[0])
print(fruit[1])
print(fruit[2])

print(fruit[2:6]) # A RANGE ELEJE INCLUSIVE, A RANGE VÉGE EXCLUSIVE!!!
print(fruit[-1])
print(fruit[-2:])
print(fruit[-1::-1]) #visszafelé kiírás


#string metódusok

print(fruit.capitalize())
print(fruit.upper())
print(fruit.title())
print(fruit.startswith("r"))




