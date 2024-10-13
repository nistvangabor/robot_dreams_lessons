#WITHOUT USING CONTEXT MANAGERS:

file = open("sample.txt", "w")  # Open file for writing
try:
    file.write("This is some sample text.")
finally:
    file.close()  # Ensure that the file is closed


#WITH USING CONTEXT MANAGERS:
with open("sample.txt", "w") as file:
    file.write("This is some sample text.\n")


# FILE HANDLING:
# WRITING TO A FILE ON NEW LINES:
with open("sample.txt", "a") as file:
    file.write("This is some sample text.\n")


#READING A FILE:
with open("sample.txt") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())


#USING A GENERATOR TO READ A FILE:
def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        print(type(file))
        for line in file:
            yield line.strip()  # Yield each line without newline characters

# Usage
file_path = 'sample.txt'  # Specify your file path here
for line in read_file_line_by_line(file_path):
    print(line)  # Process each line as needed

