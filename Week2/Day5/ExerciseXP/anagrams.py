# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:

# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.

import os
from anagram_checker import AnagramChecker


def show_menu():
    """
    Prints the menu of the program.
    """
    print("\n--- Anagram Checker ---")
    print("1. Enter a word")
    print("2. Exit")


def handle_word_input(checker: AnagramChecker):
    """
    Receives an AnagramChecker class object.
    Asks for user input.
    Validates the input and check for possible anagrams.
    """
    user_input = input("Enter a word: ").strip()
    words = user_input.split()

    if len(words) != 1:
        print("Error: Please enter exactly one word.")
        return

    word = words[0]
    if not word.isalpha():
        print("Error: only alphabetic characters are allowed.")
        return

    is_valid = checker.is_valid_word(word)
    anagrams = checker.get_anagrams(word)

    print(f"\nYOUR WORD: '{word.upper()}'")

    if is_valid:
        print("This is a valid English word.")
    else:
        print("This is not a valid English word.")

    if anagrams:
        print(f"Anagrams for your word: {', '.join(sorted(anagrams))}")
    else:
        print("No anagrams found for your word.")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    words_path = os.path.join(script_dir, "sowpods.txt")

    try:
        checker = AnagramChecker(words_path)

    except FileNotFoundError:
        print(f"Error: '{file_path}' not found.")
        return

    except UnicodeDecodeError:
        print(f"Error: '{file_path}' could not be decoded as UTF-8.")
        return

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            handle_word_input(checker)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")
