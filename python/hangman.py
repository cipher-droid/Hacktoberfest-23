import random

# List of words for the game
word_list = ["python", "hangman", "programming", "computer", "keyboard", "developer"]

def choose_word():
    return random.choice(word_list)

def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while True:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print(f"Word: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")

        if display_word == word:
            print("Congratulations! You guessed the word correctly!")
            break

        if attempts == 0:
            print(f"Sorry, you've run out of attempts. The word was '{word}'.")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess!")

if __name__ == "__main__":
    play_hangman()
