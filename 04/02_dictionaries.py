import pprint
# DICTIONARY

student = {
    "name": "John",
    "age": 20,
    "grades": [4, 5, 5],
    "major": "Computer Science",
    "is_active": True
}

pprint.pprint(student) #sorba rendezi a keye-ket!!!!

#accessing values
print(student["name"])
print(student["grades"])
print(type(student["grades"]))
last_grade = student["grades"][-1]
print(last_grade)

print(student.get("grades"))

# accessing keys
print(student.keys())
print(type(student.keys()))

#accessing values
print(student.values())
print(type(student.values()))

#adding new items to a dictionary

student["failed_exams"] = 2
print(student)
#overwrite
student["grades"].append(3)
print(student)

latest_grade = int(input("Grade: "))

us_grade_mapping = {
    5: "A",  # Excellent (Kiváló)
    4: "B",  # Good (Jó)
    3: "C",  # Satisfactory (Közepes)
    2: "D",  # Pass (Elégséges)
    1: "F"   # Fail (Elégtelen)
}

print(us_grade_mapping[latest_grade]) #először alakítsák intté!

student = ["Joe", "Rogan", 45, "male", "active"] #így nézne ki egy listában