def register_user(users, name, age = 18):
    """Register a new user"""
    user = {"name": name, "age": age}
    users.append(user)
    print(f"User registered: {user}")

def update_user_age(users, name, new_age):
    """Updates user's age"""
    for user in users:
        if user["name"] == name:
            user["age"] = new_age
            print(f"User {name}'s age has been updated to {new_age}")
            return
    else:
        print(f"No user named {name} is present in the users list")

def display_user_info(users, name):
    "Displays a single user"
    for user in users:
        if user["name"] == name:
            print(f"User info - Name: {user['name']}, Age: {user['age']}")
    

def display_all_users(users):
    "Displays all registered users"
    print("Registered users:")
    for id, user in enumerate(users):
        print(f"{id}. {user['name']} (Age: {user['age']})")


def main():

    users = []
    register_user(users=users, name="Alice")
    register_user(users=users, name="John")
    register_user(users=users, name="Dexter", age=45)
    update_user_age(users, name="Johhnny", new_age=40)
    display_user_info(users, "Alice")
    display_all_users(users)

main()