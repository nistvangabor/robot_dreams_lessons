import random

print("Welcome to the Number Guessing Game!")

# Infinite loop to keep the game running until the user decides to quit
while True:
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Ask the player how many guesses they want
    max_attempts = int(input("How many guesses do you want to try? "))
    
    # Player keeps guessing until they run out of attempts
    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt} of {max_attempts}")
        
        guess = int(input("Enter your guess (1-100): "))
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You've guessed the right number: {secret_number}")
            break  # Exit the loop if guessed correctly
        
        # Give feedback on whether the guess is too high or too low
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")
    
    # After the attempts are over, show the correct number if not guessed
    else:
        print(f"Sorry, you did not guess the number. It was: {secret_number}")
    
    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    
    if play_again != "yes":
        print("Game over! Thanks for playing!")
        break  # Exit the while loop, ending the game