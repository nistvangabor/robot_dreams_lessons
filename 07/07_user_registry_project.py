def register_user(users, name: str, age: int = 18) -> None:
    """Register a new user."""
    user = {"name": name, "age": age}  # Local variable
    users.append(user)
    print(f"User registered: {user}")

def display_user_info(users, user_id: int) -> None:
    """Display information for a specific user."""
    if user_id < len(users):
        user = users[user_id]
        print(f"User Info - Name: {user['name']}, Age: {user['age']}")
    else:
        print("User not found.")

def update_user_age(users, user_id: int, new_age: int) -> None:
    """Updates the age of the given user selected by user_id"""
    if user_id < len(users):
        users[user_id]["age"] = new_age
        print(f"Updated Age for {users[user_id]['name']} to {new_age}.")
    else:
        print("User not found.")

def display_all_users(users) -> None:
    """Display all registered users."""
    print("Registered Users:")
    for idx, user in enumerate(users):
        print(f"{idx}: {user['name']} (Age: {user['age']})")

# Main program to demonstrate functionality
def main():
    users = []  # Local variable instead of global
    register_user(users, "Alice")  # Uses default age
    register_user(users, "Bob", 22)  # Uses specified age
    display_all_users(users)  # Show all users
    display_user_info(users, 1)  # Display Bob's info
    update_user_age(users, 1, 23)  # Update Bob's age
    display_all_users(users)  # Show all users again

# Run the main function
if __name__ == "__main__":
    main()
