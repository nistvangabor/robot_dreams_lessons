import random

#BREAK:

# Generate a list of 10 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("Generated random numbers:", random_numbers)

# Loop through the list and stop at the first number divisible by 7
for number in random_numbers:
    if number % 7 == 0:
        print(f"The first number divisible by 7 is: {number}")
        break
else:
    print("No number in the list is divisible by 7.")


#CONTINUE:

number = 0

while number < 10:
    number += 1
    if number % 2 == 0:  # If the number is even
        continue  # Skip the rest of the loop for even numbers
    print(f"Processing number: {number}")


#PASS: legtöbb esetben placeholder-ként van szerepe

for i in range(5):
    if i == 3:
        pass  # Do nothing for i == 3
    else:
        print(i)

#logikusabb:

for i in range(5):
    if i != 3:
        print(i)


#ELSE: amikor végre akarunk hajtan ivalamit abban az esetben ha végigment a loop teljesen

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_for = 11

for number in numbers:
    if number == search_for:
        print(f"Found {search_for}!")
        break
else:
    print(f"{search_for} was not found in the list.")