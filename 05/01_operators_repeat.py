#arithmetic operators
a = 1 + 2 # - * / % ** stb.

#assignment:

a = 10
a += 10
a -= 10

#innentől fontos a mai óra szempontjából:
#comparison operators
a = 2
b = 3
a == b
a != b
a <= b #stb.

# logical operators

a = True
b = False
if(a and b):
    print(1)
not a and not b
a and not b

x = 9
y = 3

print(x < 10 and y == 2)
print(x < 10 or y == 2)
print(not(x < 10 and y > 5))
print(not x < 10 and y > 5)

#identity operators

print(x is y)
print(x is not y)

#identity vs comparison operator

a = 10
b = 5

print(a is b)   # False, mert az `a` és a `b` különböző memóriacímen van.
print(a == b)   # False, mert az `a` értéke nem egyenlő a `b` értékével.


x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)   # True, mert az `x` és `y` listák azonos elemeket tartalmaznak.
print(x is y)   # False, mert az `x` és `y` különböző listák a memóriában.


#x.__eq__() #erről később tanulunk hogy objektumok, amiknek metódusai és attribútumai vannak, mi alapján hasonlítódnak össze amikor az == operátort használjuk.
print(10-3*2+5)
print(10/2*5)

print(True or False and False) # az 'and' hamarabb hajtódik végre mint az or ezért True lesz az eredmény
print((True or False) and False)

# short circuit evaluation: a 60. soron lévő példában a python a True után már nem is olvassa tovább, mert a True or miatt már fixen True lesz a vége


#membership operators

print(1 in x)
print(1 not in x)
