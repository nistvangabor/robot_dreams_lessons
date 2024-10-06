numbers = [1, 2, 3, 4, 5]

print("--------------------")
#without list comprehensions:
squares = []
for num in numbers:
    squares.append(num ** 2)
print(squares) 

#with list comprehensions:
squares = [num ** 2 for num in numbers]
print(squares)

print("--------------------")
#list comprehensions with if-else:

numbers = [1, 2, 3, 4, 5]
even_squares = []
for num in numbers:
    if num % 2 == 0:
        even_squares.append(num ** 2)
print(even_squares)  # Output: [4, 16]

#with list comprehension
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print(even_squares)  # Output: [4, 16]

#list comprehension with an if-else:
numbers = [1, 2, 3, 4, 5]
new_list = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(new_list)

print("--------------------")
#measuring performance
import time

numbers = range(1, 1000000)

start = time.time()
squares_loop = []
for num in numbers:
    squares_loop.append(num ** 2)
print("For loop:", time.time() - start)

start = time.time()
squares_comprehension = [num ** 2 for num in numbers]
print("List comprehension:", time.time() - start)