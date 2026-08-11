# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# OOP (Classes, Class Methods, Inheritance)
# Modules (File Handling, String Manipulation, Data Structures)
# Text Analysis Techniques


# Key Python Topics:

# OOP (Classes, Class Methods, Inheritance)
# File handling (open())
# String manipulation (split(), join(), translate(), regular expressions)
# Dictionaries
# Sets
# Lists
# string module
# re module (regular expressions)

# Instructions:

# Create a Text class to analyze text data, either from a string or a file. Then, create a TextModification class to perform text cleaning.

# Part I: Analyzing a Simple String

# Step 1: Create the Text Class

# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g: self.text).

# Step 2: Implement word_frequency Method

# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.

# Step 3: Implement most_common_word Method

# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.

# Step 4: Implement unique_words Method

# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.

# Part II: Analyzing Text from a File

# Step 5: Implement from_file Class Method

# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.

# Bonus: Text Modification

# Step 6: Create the TextModification Class

# Create a class called TextModification that inherits from Text.

# Step 7: Implement remove_punctuation Method

# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.

# Step 8: Implement remove_stop_words Method

# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.

# Step 9: Implement remove_special_characters Method

# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.

import string
import re
import os


class Text:
    def __init__(self, text: str):
        self.text = text

    def word_frequency(self, word):
        list_of_words = self.text.split()
        frequency = list_of_words.count(word)

        if frequency > 0:
            return frequency

        print(f"Given word '{word}' was not found in the text.")
        return None

    def most_common_word(self):
        list_of_words = self.text.split()
        word_frequencies = {}

        for word in list_of_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

        return max(word_frequencies, key=word_frequencies.get)

    def unique_words(self):
        list_of_words = self.text.split()
        set_of_words = set(list_of_words)

        return list(set_of_words)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as file:
            content = file.read()

        return cls(content)

    def __str__(self):
        return self.text


class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)

    def remove_punctuation(self):
        pattern = f"[{re.escape(string.punctuation)}]"

        return re.sub(pattern, "", self.text)

    def remove_stop_words(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        stop_words_path = os.path.join(script_dir, "stop_words_english.txt")

        with open(stop_words_path, "r", encoding="utf-8") as f:
            content = f.read()
            stop_words = set(content.split())

        list_of_words = self.text.split()
        filtered_words = [
            word for word in list_of_words if word.lower() not in stop_words
        ]

        modified_text = " ".join(filtered_words)

        return modified_text

    def remove_special_characters(self):
        return re.sub(r"[^a-zA-Z0-9\s]", "", self.text)


test_cases = [
    "the quick brown fox jumps over the lazy dog the fox runs",
    "cat dog cat dog bird",
    "hello    world hello   there hello",
    "Apple apple APPLE banana Banana apple!",
]

for text in test_cases:
    analyzer = Text(text)
    print(f"{text} -> {analyzer.most_common_word()}")
    print(f"{text} -> {analyzer.unique_words()}")

text_obj = Text.from_file("C:\DI-Bootcamp\Week2\Day4\ExerciseXP\words.txt")

text = TextModification(
    "This is a simple test of the stop words removal method and it should work well"
)

print(text.remove_punctuation())

print(text.remove_stop_words())
