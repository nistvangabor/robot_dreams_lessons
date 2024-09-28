# az eredeti feladat egy loop-ot is tartalmaz, ezzel a következő órán kiegészítjük

#‘FizzBuzz’ if i is divisible by 3 and 5,
#‘Fizz’ if i is divisible by 3,
#‘Buzz’ if i is divisible by 5
#‘i’ as a string, if none of the conditions are true.


n = 15

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(str(n))

#### felcserélve

if n % 3 == 0:
    print("Fizz")
elif n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(str(n))