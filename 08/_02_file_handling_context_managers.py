import os
#OPENING A FILE FOR WRITING WITHGOUT CONTEXT MANAGERS:
print(os.getcwd())

file = open("08/sample.txt", "w")

try:
    file.write("This is some sample text")
finally:
    file.close()


#WITH CONTEXT MANAGERS:
with open("08/sample.txt", "w") as file:
    file.write("This is some sample text.\n")


# FILE HANDLING: WRITING TO A FILE ON NEW LINES:
with open("08/sample.txt", "a") as file:
    file.write("This is some sample text as well \n")


# FILE HANDLING: READING A FILE:
with open("08/sample.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line.strip())


# USING A GENERATOR TO READ A FILE:
print("-----------------------------")
def read_file_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


file_path = "08/sample.txt"
gen = read_file_line_by_line(file_path=file_path)
print(next(gen))
print(next(gen))

for line in read_file_line_by_line(file_path=file_path):
    print(line)
