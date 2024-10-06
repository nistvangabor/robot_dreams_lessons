#PARAMETERS

def greet(name):
    print(f"Hello, {name}!")

greet("Johnny") # Johnny = argumentum amit megkap a name parameter


#positional parameters:

def add(x,y):
    return x + y

result = add(3, 5) # pozíció alapján lesz a 3-ból x, és az 5-ből y
result = add(5, 3) # fordítva

#default parameters:
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, Guest!
greet("Bob")  # Output: Hello, Bob!

print("-------------------------------------")
#combining positional and default parameters
def show_book_details(title, author="Unknown", year=2020):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")

show_book_details("Test Book")
show_book_details("Test Book", "Test Author")
show_book_details("Test Book", "Test Author", 2024)


#ARGUMENTS:

#keyword arguments:

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a(n) {animal_type} named {pet_name}")

describe_pet(pet_name="Max")
describe_pet(animal_type="dog", pet_name="Rusty")


#positional only and keyword only
def test_function(a, b, /, *, c, d):
  return a + b + c + d

test_function(5, 6, c = 7, d = 8)
#test_function(5, b=6, c=8, d = 8) #error

print("--------------------------------------------")
#DANGER ZONE: mutable objects as default parameters:
#A default paraméterek akkor kapják meg az értéküket amikor a function definiálódik, nem 
# minden alkalommal amikor meghívjuk. Ezért mutable object-eknél ahelyett hogy minden hozzáadás új 
# üres listához adódna hozzá, ugyanaz a lista lesz használva minden hívásnál.
#WRONG:
def append_to_list(value, my_list=[]): # 
    my_list.append(value)
    return my_list

print(append_to_list(1))  # Output: [1]

print(append_to_list(2))  # Output: [1, 2] - Unexpected behavior

print(append_to_list(3))  # Output: [1, 2, 3] - Still unexpected

#SOLUTION:
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

print(append_to_list(1))  # Output: [1]

print(append_to_list(2))  # Output: [2]

print(append_to_list(3))  # Output: [3]