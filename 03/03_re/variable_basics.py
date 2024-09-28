#VÁLTOZÓK / VARIABLES

name = "Jim"
age = 25
print(name, age)

#assignment operator (=, !=, >, < stb.)
#arithmetic operator (+, -, *, / stb.)

age = 25 + 1
print(age)


a = 10
b = 4
area = a * b
print("area: ", area)


#NAMING CONVENTIONS:

camelCaseVariableName = "" #BAD PRACTICE -> CAMEL CASE
snake_case_variable_name = "" #GOOD PRACTICE -> SNAKE CASE

# KONSTANS

PI = 3.14
MAX_ROUNDS = 3


#Dynamically typed / dinamikusan típusos

number = 10
print(number)
number = "apple"
print(number)

# pointers

my_var = 15
print(id(my_var))
my_var2 = 15
print(id(my_var2))

my_var = 16
print(id(my_var))
print("---------------")
x = 5
y = x #5
print(id(x))
print(id(y))
print("X értéke megváltozik")
x = 10
print(y)
print(id(x))
print(id(y))

#GARBAGE COLLECTION
x = 1000 # 
y = 2000 # itt már nem elérhető az 1000 a memóriában, mert nincs tovább szükség rá


