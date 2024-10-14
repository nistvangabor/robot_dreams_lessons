def divide_numbers(a, b):
    return a / b

#zero division error
num = divide_numbers(a=10, b=1)
print(num)

#value rror
#age = float(input("How old are you? Please provide a number!"))
#print(age)

#index error
#my_list = [1,2,3,4,5]
#print(my_list[5])

#HANDLING EXCEPTIONS:

try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    c = a / b
except ZeroDivisionError as e:
    print(f"Zero div. error: {e}")
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:
    print(f"Something unexpected happened: {e}")
else:
    print(c)
finally:
    print("Division attempt finished.")


print("Random stuff")

# RAISING EXCEPTIONS:

def calculate_rectangle_area(a, b):
    return a * b


area = calculate_rectangle_area(10, 5)
area_error = calculate_rectangle_area(10, -1)
print(area_error)
#area_error_2 = calculate_rectangle_area("ten", "two")
#print(area_error_2)


#SOLVE ISSUES:

def calculate_rectangle_area(length, width):

    if not isinstance(length, (int, float)) or not isinstance(width, (int,float)):
        raise TypeError("Both params must be a number!")

    if length >= 0 or width >= 0:
        raise ValueError("Both params must be a positive number!")

    return length * width


#example usage:

try:
    area = calculate_rectangle_area(5,"two")
    print(f"Area of the rectangle: {area}")
except ValueError as e:
    print(f"Value error: {e}")
except TypeError as e:
    print(f"Type error: {e}")


#custom exception-ök: OOP tudás szükséges.