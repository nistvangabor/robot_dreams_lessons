import math
#function-ök/funckiók

#len()
print(len("this is a random string"))

word_1 = "apples"
word_2 = "oranges"

sum_length = len(word_1) + len(word_2)
print(sum_length)


# concatenation / konkatenálás (összefűzés)
first_name = "Istvan Gabor"
last_name = "Nagy"
full_name = first_name + " " + last_name
print(full_name)
introduction = "My name is " + first_name + " " + last_name + "."
# f-string / interpolált string
better_introduction = f"My name is {first_name} {last_name}."

# string slicing, ez később a listáknál hasznos lesz!

fruit = "apple" #was originally "apple"
print(fruit[0])
print(fruit[3])
print(fruit[4])
print(fruit[-1])

print(fruit[4:-1]) #a range eleje inklúzív, a range vége exklúzív (magyarul a kezdőérték beletartozik, míg a záró nem)
print(fruit[4:])
print(fruit[-2:])
print(fruit[-2:-5:-1]) #backwards slicing (start index, end index, step size)

# string metódusok

fruit = "apple" #originally it is just apple
print(fruit.capitalize())
print(fruit.upper()) #lower()
fruit = "apple banana" #originally it is just apple
print(fruit.title())
fruit = " apple banana "
print(fruit.strip())
print(fruit.startswith(" a"))
print(fruit.endswith("a "))

changed_fruit = fruit.replace("p", "b") # never happens in-place, always need to reassign
print(changed_fruit)
a_index = fruit.find("a")
print(a_index)

print(fruit)
#method chaining:
fruit.capitalize().strip()






