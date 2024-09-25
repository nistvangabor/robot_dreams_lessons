import math
#assignment operators

a = 10
a += 10 #rövidítése annak hogy a = a + 10
print(a)

#arithmetic operators

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

# logical operátorok

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


#identity, membership, bitwise, ternary operátorokról később!