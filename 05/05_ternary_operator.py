number = 5

if number > 5:
    result = "greater than 5"
else:
    result = "5 or less"
print(result)

#ugyanez a ternary operátorral:
result = "greater than 5" if number > 5 else "5 or less"
print(result)


#megmutatni, hogy a 02_if_else végén létrehozott megvadulós példa nem jó ternary-hoz

age = 65

category = "Minor" if age < 18 else "Adult" if age < 65 else "Senior"
print(category)  #ezt már nem raknám bele egy ternary-ba