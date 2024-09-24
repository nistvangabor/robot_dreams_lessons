#VÁLTOZÓK / VARIABLES

name = "Jim"
age = 25
print(age)
age = 25 + 1
print(age)

##########

a = 10
b = 5
area = a * b
print(area)

########## VARIABLE NAMING CONVENTIONS
#variable style guide PEP-8: https://peps.python.org/pep-0008/

camelCaseVariableName = "" #BAD PRACTICE, NEM HASZNÁLJUK PYTHON-ban
correct_variable_name = "" #GOOD PRACTICE
current_user_score = 1

#KONSTANSOK
PI = 3.14
MAX_ROUNDS = 3 # maximum number of rounds which can be played in a given game / maximum ennyi kör játszható egy adott játékban

#dynamically typed / dinamikus típusosság
x:int = 10
x = "dog"
print(x)

### mi történik a háttérben? #pointers
print("--------------------")
my_var = 15
print(id(my_var))

my_var_2 = 15 # eredetileg 30 volt
print(id(my_var_2))

my_var_2 = 30
print(id(my_var_2))

x = 5
y = x

print(id(x))
print(id(y))

x = 10

print(x)
print(y)

print(id(x))
print(id(y))

#GARBAGE COLLECTION
x = 1000
x = 2000 # the memory holding 1000 can be garbage collected, as it is no longer needed / az 1000 törölhető a memóriából, mert nincs többé szükség rá




