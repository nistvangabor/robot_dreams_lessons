import math
#function-ök/funckiók

#len()
print(len("this is a random string"))

word_1 = "apples"
word_2 = "oranges"

sum_length = len(word_1) + len(word_2)
print(sum_length)

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

#operátorok (arithmetic operators, search for python operators):

a = 10
b = 2

multipled_result = a * b
divided_result = a / b
added_result = a + b
substracted_result = a - b
modulus = a % b
exponentiation = a ** 2
square_root = a ** (1/2)
sqrt = math.sqrt(10)
print("modulus: ", modulus)
print("exponentiation:", exponentiation)
print("square_root:", square_root)
print("math module square_root:", sqrt)


#egyéb típuskonverzióra használható függvények:
float()
str()
int()
bool()

# concatenation / konkatenálás (összefűzés)
first_name = "Istvan Gabor"
last_name = "Nagy"
full_name = first_name + " " + last_name
print(full_name)

# f-string / interpolált string

full_name = f"{first_name} {last_name}" 
print(full_name)

# string slicing, ez később a listáknál hasznos lesz!

fruit = "raspberryyyyyyyyyyyyyyyyyyyyyyy" #was originally "apple"
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

#truthy-falsy értékek
print(bool(1))
print(bool(0))

print(bool(""))
print(bool("something"))

# boolean operátorok

a = True
b = False

print(a and b)
print(a or b)
print(not True)

#comparison / összehasonlító operátorok

a = 10
b = 5

print(a < b)
print(a == b)
print(a > b)
print(a != b)
print(a >= b)
print(a <= b)


