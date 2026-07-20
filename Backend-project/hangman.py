# Hangman Game Console Application
# Demonstrates: variables, conditionals, loops, lists, functions, file operations

import random

RESULTS_FILE = "hangman_results.txt"

# List of predefined words (criteria: arrays/lists)
WORDS = ["python", "github", "keyboard", "monitor", "backend", "function"]

MAX_ATTEMPTS = 6  # maximum wrong guesses allowed


def choose_word():
    # Pick a random word from the predefined list
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    # Build the display string: show guessed letters, hide others with _
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "
    return result.strip()


def get_valid_letter(guessed_letters):
    # Ask for a letter and validate the input
    while True:
        letter = input("Guess a letter: ").lower().strip()
        if len(letter) != 1:
            print("Please enter exactly one letter.")
        elif not letter.isalpha():
            print("Please enter a letter (a-z), not a number or symbol.")
        elif letter in guessed_letters:
            print("You already guessed that letter, try another one.")
        else:
            return letter


def play_game():
    # One full round of Hangman; returns True if player won
    word = choose_word()
    guessed_letters = []  # list of letters the player has tried
    wrong_attempts = 0

    print("\nThe word has", len(word), "letters.")

    while wrong_attempts < MAX_ATTEMPTS:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Wrong attempts: {wrong_attempts}/{MAX_ATTEMPTS}")

        letter = get_valid_letter(guessed_letters)
        guessed_letters.append(letter)

        if letter in word:
            print("Correct letter!")
        else:
            wrong_attempts += 1
            print("Wrong letter!")

        # Check if all letters of the word are guessed
        if all(l in guessed_letters for l in word):
            print(f"\nYou won! The word was '{word}'.")
            return True

    print(f"\nGame over! The word was '{word}'.")
    return False


def save_result(won):
    # Append the game result to the results file (file creation/editing)
    with open(RESULTS_FILE, "a", encoding="utf-8") as file:
        if won:
            file.write("Game result: WIN\n")
        else:
            file.write("Game result: LOSS\n")


def show_results():
    # Read and display all saved results
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            if content:
                print("\n--- Game Results ---")
                print(content)
            else:
                print("No results yet.")
    except FileNotFoundError:
        print("No results file found yet.")


def clear_results():
    # Delete all saved results (file deleting skill)
    open(RESULTS_FILE, "w").close()
    print("Results cleared.")


def main():
    # Main menu loop
    while True:
        print("\n===== Hangman =====")
        print("1 - Play game")
        print("2 - Show results")
        print("3 - Clear results")
        print("4 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            won = play_game()
            save_result(won)
        elif choice == "2":
            show_results()
        elif choice == "3":
            clear_results()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


main()