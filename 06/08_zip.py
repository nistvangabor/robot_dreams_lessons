# List of student names
students = ["Alice", "Bob", "Charlie", "David"]

# List of corresponding scores
scores = [85, 90, 78, 88]

# Using zip to iterate over both lists simultaneously
for student, score in zip(students, scores):
    print(f"{student} scored {score} points.")

#addig megy amíg a legrövidebb iterable kimerül