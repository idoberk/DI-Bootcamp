# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Python Basics
# String Manipulation
# Lists
# Sorting
# Functions
#
# Challenge 1: Sorting
#
# Instructions:
#
# Write a Python program that takes a single string of words as input, where the words are separated by commas (e.g., ‘apple,banana,cherry’). The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.
#
# Step 1: Get Input
#
# Use the input() function to get a string of words from the user.
# The words will be separated by commas.
#
# Step 2: Split the String
#
# Step 3: Sort the List
#
# Step 4: Join the Sorted List
#
# Step 5: Print the Result
#
# Print the resulting comma-separated string.
#
# Expected Output:
#
# If the input is without,hello,bag,world, the output should be bag,hello,without,world.


def get_valid_words():
    user_input = input("Enter words separated by commas: ")
    words = [word.strip() for word in user_input.split(",")]

    for i, word in enumerate(words):
        while not word.isalpha():
            print(f'"{word}" is invalid. It must contain only letters.')
            word = input(f"Please re-enter word #{i + 1}: ").strip()
        words[i] = word

    return words


def sorting_challenge():
    word_list = get_valid_words()
    word_list.sort()
    string_result = ",".join(word_list)

    print(string_result)


sorting_challenge()

# Challenge 2: Longest Word
#
# Instructions:
#
# Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.
#
# Step 1: Define the Function
#
# Define a function that takes a string (the sentence) as a parameter.
#
# Step 2: Split the Sentence into Words
#
# Step 3: Initialize Variables
#
# Step 4: Iterate Through the Words
#
# Step 5: Compare Word Lengths
#
# Step 6: Return the Longest Word
#
# Expected Output:
#
# longest_word("Margaret's toy is a pretty doll.") should return "Margaret's".
# longest_word("A thing of beauty is a joy forever.") should return "forever.".
# longest_word("Forgetfulness is by all means powerless!") should return "Forgetfulness".
#
# Key Python Topics:
#
# Functions
# Strings
# .split() method
# Loops (for)
# Conditional statements (if)
# String length (len())


def longest_word_challenge(sentence: str):
    words_list = [word.strip() for word in sentence.split(" ")]
    longest_word = words_list[0]
    longest_word_len = len(longest_word)

    for word in words_list:
        if len(word) > longest_word_len:
            longest_word = word

    return longest_word


sentence = input("Enter any sentence you'd like: ").strip()
longest_word = longest_word_challenge(sentence)
print(longest_word)
