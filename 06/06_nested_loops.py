# Seating chart represented as a 2D list (list of lists)
seating_chart = [
    ["Alice", "Bob", "Charlie"],
    ["David", "Eva", "Frank"],
    ["Grace", "Henry", "Isabel"]
]

# Outer loop goes through each row (list of students in each row)
for row in seating_chart:
    # Inner loop goes through each student in the row
    for student in row:
        print(student, end="\n")
    # Print a newline after each row
    print()