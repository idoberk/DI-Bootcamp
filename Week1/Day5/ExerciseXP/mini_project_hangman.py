# What you will learn
# Conditionals
# Loops
# Functions
# Modules
#
# What you will create
# Use python to create a Hangman game.
#
# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.
#
# Starter code
# Here is a piece of code that will give you a random word.
#
#     import random
#
#     wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
#     word = random.choice(wordslist)

### YOUR CODE STARTS FROM HERE ###

import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]


def get_valid_guess(prompt: str):
    """Repeatedly ask for a valid guess."""
    guess = None

    while guess is None:
        try:
            guess = input(prompt).strip().lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Guess must only include a single alphabetical character.")
                guess = None
        except ValueError:
            print("Invalid input. Please enter an alphabetical character.")

    return guess


def get_random_word():
    wordslist = [
        "correction",
        "childish",
        "beach",
        "python",
        "assertive",
        "interference",
        "complete",
        "share",
        "credit card",
        "rush",
        "south",
    ]

    return random.choice(wordslist)


def check_win(guess_word):
    if "*" not in guess_word:
        print("You win!")
        return True


def play():
    display = []
    guessed_letters = []
    word = get_random_word()
    word_length = len(word)
    lives = 6
    end_of_game = False

    for index in range(word_length):
        display.append("*")

    display_word = "".join(display)

    print(f"{display}")

    while not end_of_game:
        guess = get_valid_guess("Guess a letter: ")
        if guess in guessed_letters:
            print(f"The letter '{guess}' was already used.\n")
            continue
        else:
            guessed_letters.append(guess)

            for index in range(word_length):
                character = word[index]
                if guess == character:
                    display[index] = character
                    display_word = "".join(display)
            if guess not in word:
                lives -= 1
                print(stages[lives])
                print(f"The letter '{guess}' is not in the word.\n")
            print(f"{display}\n")
            if lives == 0:
                end_of_game = True
                print("You ran out of lives, you lose!")
                print(f'The word was "{word}"')
        if check_win(display):
            end_of_game = True


play()
