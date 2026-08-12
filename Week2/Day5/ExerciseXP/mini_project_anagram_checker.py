# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# OOP (Classes, Methods)
# Python Files I/O (Reading Files)
# String Manipulation
# Algorithm Design (Anagram Checking)
# Key Python Topics:

# OOP (Classes, Methods)
# File I/O (Reading Files)
# String Manipulation (strip(), split(), isalpha())
# Algorithm Design (Anagram Checking)
# User Input and Validation
# Conditional Logic
# Loops

# 🛠️ What you will create
# An anagram checker program that takes user input, validates it, and finds anagrams from a word list.

# Instructions:

# Download the provided text file (word list).
# Create anagram_checker.py with the AnagramChecker class.
# Create anagrams.py for the user interface.
# anagram_checker.py:

# Step 1: Create the AnagramChecker Class

# Create a class called AnagramChecker.
# Implement the __init__ method:
# Load the word list file into a variable (e.g., a set or list).
# Store the words in lowercase for case-insensitive comparison.

# Step 2: Implement is_valid_word Method

# Create a method called is_valid_word(word).
# Check if the given word exists in the loaded word list (case-insensitive).
# Return True if valid, False otherwise.

# Step 3: Implement is_anagram Method

# Create a method called is_anagram(word1, word2).
# Check if the sorted characters of word1 are equal to the sorted characters of word2.
# Return True if anagrams, False otherwise.

# Step 4: Implement get_anagrams Method

# Create a method called get_anagrams(word).
# Create an empty list to store anagrams.
# Iterate through the word list.
# For each word in the list, check if it’s an anagram of the given word using is_anagram.
# If it’s an anagram and not the same word, add it to the anagrams list.
# Return the list of anagrams.

# anagrams.py:

# Step 1: Import AnagramChecker

# Step 2: Create a Menu Loop

# Step 3: Get User Input and Validate

# Step 4: Find and Display Anagrams

# Create an instance of AnagramChecker.
# Use is_valid_word to check if the word is valid.
# Use get_anagrams to find anagrams.
# Display the word, its validity, and the anagrams in a formatted message.

# First Download this text file

# Create a new file called anagram_checker.py which contains a class called AnagramChecker.

# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.

# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)

# Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.

# Note: None of the methods in the class should print anything.

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

from anagrams import main

if __name__ == "__main__":
    main()
