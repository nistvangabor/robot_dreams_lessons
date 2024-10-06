#ARBITRARY ARGUMENTS: *args

def sum_numbers(*args):
    return sum(args)

result = sum_numbers(1,2,3,4,5)
print(result)
result = sum_numbers(10,34,56765,234)
print(result)

#ARBITRARY KEYWORD ARGUMENTS: **kwargs

def describe_person(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=30, job="Engineer")


#combining everything
def introduce_person(name, age, *hobbies, country="Unknown", **additional_info):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Country: {country}")
    
    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f"  - {hobby}")
    
    if additional_info:
        print("Additional Information:")
        for key, value in additional_info.items():
            print(f"  {key}: {value}")

introduce_person("John", 30, "reading", "hiking",
                country="USA",
                occupation="Engineer",
                pet="Dog")


