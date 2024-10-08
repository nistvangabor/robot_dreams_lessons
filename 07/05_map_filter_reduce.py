from functools import reduce

#MAP: lefuttatja a megadott function-t egy iterable minden elemére, és egy iterator-t ad vissza ami átkonvertálható pl listává

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))#megmutatni hogy ezt listává is tudom alakítani
#print(next(squared_numbers))
#print(next(squared_numbers))
print(squared_numbers)
#extra: list comprehension-ben való function hívás
squared_numbers = [square(num) for num in numbers]
print(squared_numbers)


#FILTER: 

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))

print(even_numbers)  # Output: [2, 4]

#REDUCE

# Let's say you have some numbers
numbers = [1, 2, 3, 4]

# This function will add two numbers together
def add(x, y):
    return x + y

# Now, let's use reduce to add all the numbers together
total = reduce(add, numbers)
print(total)  # Output: 10


#HA LESZ IDŐ:

#higher order functions can do 2 things:
#1.using functions as arguments

def color_shape(color_function, shape):
    print(color_function(shape))

def blue_shape(shape):
    return f"The {shape} is colored blue."

# Here, we're using blue_shape as an argument in color_shape
color_shape(blue_shape, "circle")


#2.returning functions
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = make_multiplier(2)  # This creates a function that doubles numbers
triple = make_multiplier(3)   # This creates a function that triples numbers

print(double(5))  # Output: 10 (2 * 5)
print(triple(5))  # Output: 15 (3 * 5)