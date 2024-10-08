#function without return value
def example_function():
    print("This is a function")

value = example_function() # no need to assign to a variable as it returns None
print(value)
print(type(value))


#function with return value
def add(a, b):
    sum = a + b
    return sum

num = add(1,2)
print(num)
print(type(num))

#return early

def calculate_age_in_days(age):
    if age < 0:
        print("Invalid age! Age cannot be negative.")
        return 
    
    age_in_days = age * 365
    print(f"User is approximately {age_in_days} days old.")

    return age_in_days

# Example usages
age_in_days = calculate_age_in_days(-5)  # Invalid case, will exit early
print(age_in_days)
age_in_days = calculate_age_in_days(25)  # Valid case, continues to the rest of the function
print(age_in_days)


#returning multiple values
def multiply_two_values(a, b):
    return a*2, b*2 #returns a tuple

print(type(multiply_two_values(1,2)))

#tuple unpacking
x,y = multiply_two_values(1,2)
