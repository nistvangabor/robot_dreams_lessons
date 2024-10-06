# mire jók a function-ök?
# - kód újrahasznosítás
# - kód rendezettségének fokozása
# - "separation of concerns" - különböző feladatok function-ökre bontása
# dolgok amiket tartsunk be:
# - DRY (Don't Repeat Yourself) -> repetitív logika abasztrakciója function-ökkel
# - Single Responsibility Principle -> egy function csak egy feladatért legyen felelős
# - Avoid mutable objects as default arguments!


#BAD EXAMPLE
name_1 = "John"
print(f"Hello {name_1}, welcome back!")

name_2 = "Jane"
print(f"Hello {name_2}, welcome back!")

name_3 = "Mike"
print(f"Hello {name_3}, welcome back!")


#GOOD EXAMPLE:
print("------------------------")
def greet_user(name):
    print(f"Hello {name}, welcome back!")

name_1 = "John"
name_2 = "Jane"
name_3 = "Mike"

greet_user(name_1)
greet_user(name_2)
greet_user(name_3)

#OR EVEN USE LISTS AND LOOPS:
print("------------------------")
names = ["John", "Jane", "Mike"]
for name in names:
    greet_user(name)