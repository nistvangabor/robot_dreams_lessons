import random

print("Welcome to the Number Guessing Game!")

# Ask how many rounds to play
rounds = int(input("How many rounds would you like to play? "))

# Loop through the number of rounds
for round_number in range(1, rounds + 1):
    print(f"\nRound {round_number}!")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Ask the player how many guesses they want
    max_attempts = int(input("How many guesses do you want to try? "))
    
    # Variable to store whether the user guessed correctly
    guessed_correctly = False

    # Inner loop: Player keeps guessing until they run out of attempts
    for attempt in range(1, max_attempts + 1):
        print(f"Attempt {attempt} of {max_attempts}")
        
        guess = int(input("Enter your guess (1-100): "))
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You've guessed the right number: {secret_number}")
            guessed_correctly = True
            break  # Break the loop if guessed correctly
        
        # Give feedback on whether the guess is too high or too low
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")
    
    # After the attempts are over, show the correct number if not guessed
    if not guessed_correctly:
        print(f"Sorry, you did not guess the number. It was: {secret_number}")
    
    # Ask the player if they want to continue to the next round
    continue_game = input("Do you want to continue to the next round? (yes/no): ").lower()
    if continue_game != "yes":
        print("Thanks for playing!")
        break  # Exit the outer loop and end the game

print("Game over! Hope you had fun!")