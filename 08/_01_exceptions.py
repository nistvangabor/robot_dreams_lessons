def divide_numbers(a, b):
    return a / b 


#num = divide_numbers(10,0) #először megpróbálni rendes pozitív számmal
#print(num)

#age = float(input("How old are you? Please provide a number!"))

my_list = [1,2,3,4]
#print(my_list[6])


a = 10
b = 0
#c = a / b

#HANDLING EXCEPTIONS:

try:
    a = float(input("Add meg az első számot!"))
    b = float(input("Add meg a második számot!"))
    c = a / b
except ZeroDivisionError as e:
    print(f"Error: B is a 0. {e}")
except ValueError as e:
    print(f"Error: can not convert to float. {e}")
except Exception as e:
    print(f"Something unexpected happened. {e}")
else:
    print(c)
finally: 
    print("Division attempt finished.")


#RAISING EXCEPTIONS

def calculate_rectangle_area(a, b):
    return a * b

area = calculate_rectangle_area(10, 5)
print(area)

#area = calculate_rectangle_area("ten", "five")
area = calculate_rectangle_area(-1, 5)
print(area)

#SOLVE ISSUES:

def calculate_rectangle_area(length, width):
    # Check if the inputs are valid numbers
    if not isinstance(length, (int, float)):
        raise TypeError("Length must be a number.")
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be a number.")

    # Check if the dimensions are positive
    if length <= 0:
        raise ValueError("Length must be a positive number.")
    if width <= 0:
        raise ValueError("Width must be a positive number.")

    # Calculate and return the area
    return length * width

# Example usage
try:
    area = calculate_rectangle_area(5, 2)  # This will raise a ValueError
    print(f"Area of the rectangle: {area}")
except ValueError as ve:
    print(f"ValueError: {ve}")
except TypeError as te:
    print(f"TypeError: {te}")



#CUSTOM EXCEPTION-ÖKet is lehet írni, de ehhez ismerni kell a class-okat.