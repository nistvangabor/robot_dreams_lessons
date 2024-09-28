# syntax
condition = True

if condition == True:
    print("The condition is true.")
else:
    print("The condition is false.")

# truthy-falsy értékek miatt nem feltétlenül kell az == operátor:

if condition:
    print("The condition is true.")
else:
    print("The condition is false.")


number = 1

if number:
    print(f"The value of a is other than 0: {number}")
else:
    print(f"The value of a is 0: {number}")


numbers = [1,2,3] #eredetileg 0 volt

print(bool(numbers))

if numbers: #ahelyett hogy if len(numbers) > 0
    print(f"There are values in the list: {numbers}")
else:
    print("The list is empty!")


# if-elif-else using arithmetic operators

number = 10 #amint az if-else megtalálja az értéket, kilép a statementből és tovább olvassa a kódot

if number == 10:
    print("The number is 10")
elif number == 13:
    print("The number is 13")
elif number == 15:
    print("The number is 16")
else:
    print(f"The number is something else: {number}")



# if-elif-else using membership and logical operators

fruits = ["raspberry", "banana", "cherry", "watermelon"]

if "raspberry" in fruits:
    print("Raspberry is present int the fruits list")



if "raspberry" in fruits or "banana" in fruits:
    print("either of the 2 is present in the list")


if "raspberry" in fruits and "banana" not in fruits:
    print("either of the 2 is present in the list")
elif "cherry" in fruits:
    print("at least we have cherry!")


#if-elif-else using identity operators:
a = 1
b = 2 # eredetileg 2 volt

if a is b:
    print("The 2 objects are the same")

if a is not b:
    print("The 2 objects are not the same")

c = 3

# combining multiple operators in a single statement

if (a is not b and c == 3 and ("cherry" in fruits or "elderflower" in fruits)):
    print("All these things are true")