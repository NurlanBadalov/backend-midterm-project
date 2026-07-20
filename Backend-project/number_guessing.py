# Number Guessing Game Console Application
# Demonstrates: variables, conditionals, loops, lists, functions, file operations

import random

RESULTS_FILE = "game_results.txt"

MIN_NUMBER = 1    # lower bound of the range
MAX_NUMBER = 100  # upper bound of the range


def get_valid_guess():
    # Ask for a number and validate the input (must be a whole number)
    while True:
        user_input = input(f"Guess a number ({MIN_NUMBER}-{MAX_NUMBER}): ")
        if user_input.isdigit():
            guess = int(user_input)
            if MIN_NUMBER <= guess <= MAX_NUMBER:
                return guess
            print(f"Number must be between {MIN_NUMBER} and {MAX_NUMBER}.")
        else:
            print("Invalid input! Please enter a whole number.")


def play_round():
    # One full round of the game; returns the number of attempts used
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)  # random secret number
    guesses = []  # list of all guesses this round

    while True:
        guess = get_valid_guess()
        guesses.append(guess)  # store every guess in the list

        if guess < secret_number:
            print("Higher!")
        elif guess > secret_number:
            print("Lower!")
        else:
            print(f"Correct! You found it in {len(guesses)} attempts.")
            print("Your guesses were:", guesses)
            return len(guesses)


def save_result(attempts):
    # Append the result of a round to the results file (file creation/editing)
    with open(RESULTS_FILE, "a", encoding="utf-8") as file:
        file.write(f"Round finished in {attempts} attempts\n")


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
        print("\n===== Number Guessing Game =====")
        print("1 - Play game")
        print("2 - Show results")
        print("3 - Clear results")
        print("4 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            attempts = play_round()
            save_result(attempts)
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