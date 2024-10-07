count = 0
while count < 5:
    print(count)
    count += 1


#infinite loop:
#while True:
#    print("This loop will run forever!")


#asking a user until a good answer is given

while True:
    answer = input("Do you want to be a Python dev? yes/no: ")
    if answer in ["yes", "no"]:
        break

print("This is running after the loop finished")