import random

# Set the range for the random number
min_number = 1
max_number = 100
secret_number = random.randint(min_number, max_number)

# Set the number of attempts
max_attempts = 10
attempts = 0

print(f"Welcome to Guess the Number! I'm thinking of a number between {min_number} and {max_number}.")

while attempts < max_attempts:
    try:
        # Get the player's guess
        guess = int(input("Enter your guess: "))

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number, which was {secret_number}.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Remaining attempts: {remaining_attempts}")

    except ValueError:
        print("Invalid input. Please enter a number.")

if attempts == max_attempts:
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
