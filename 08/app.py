import random
import setup_logger

logger = setup_logger.setup_logger("root")
print(__name__)
def get_max_attempts():
    """Ask the player for the number of attempts and handle invalid input."""
    while True:
        try:
            max_attempts = int(input("How many guesses do you want to try? "))
            if max_attempts <= 0:
                raise ValueError("Number of guesses must be greater than zero.")
            return max_attempts
        except ValueError as e:
            logger.error(f"Invalid input for max_attempts: {e}")

def get_player_guess():
    """Ask the player for a guess and handle invalid input."""
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                raise ValueError("Guess must be between 1 and 100.")
            return guess
        except ValueError as e:
            logger.error(f"Invalid input for guess: {e}")

def play_game():
    """Main function to run the game."""
    secret_number = random.randint(1, 100)
    max_attempts = get_max_attempts()

    for attempt in range(1, max_attempts + 1):
        logger.info(f"Attempt {attempt} of {max_attempts}")

        guess = get_player_guess()

        # Check if the guess is correct
        if guess == secret_number:
            logger.info(f"Congratulations! You've guessed the right number: {secret_number}")
            break
        elif guess > secret_number:
            logger.info("Too high!")
        else:
            logger.info("Too low!")
    else:
        logger.info(f"Sorry, you did not guess the number. It was: {secret_number}")

def main():
    """The main game loop."""
    logger.info("Welcome to the Number Guessing Game!")
    
    while True:
        try:
            play_game()
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
        
        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            logger.info("Game over! Thanks for playing!")
            break

if __name__ == "__main__":
    main()