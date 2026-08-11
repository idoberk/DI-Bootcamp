# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# File handling (reading files)
# Data structures (lists)
# Random number generation
# String manipulation
# JSON (parsing, modifying, and saving)

# 🌟 Exercise 1: Random Sentence Generator
# Goal: Create a program that generates a random sentence of a specified length from a word list.

# Key Python Topics:

# File handling (open(), read())
# Lists
# Random number generation (random.choice())
# String manipulation (split(), join(), lower())
# Error handling (try, except)
# Input validation

# Instructions:

# Download the provided word list and save it in your development directory.
# Create a function to read the words from the file.
# Create a function to generate a random sentence of a given length.
# Create a main function to handle user input and program flow.

# Step 1: Create the get_words_from_file function

# Create a function named get_words_from_file that takes the file path as an argument.
# Open the file in read mode ("r").
# Read the file content.
# Split the content into a list of words.
# Return the list of words.

# Step 2: Create the get_random_sentence function

# Create a function named get_random_sentence that takes the sentence length as an argument.
# Call get_words_from_file to get the list of words.
# Select a random word from the list length times.
# Create a sentence with the selected words.
# Convert the sentence to lowercase.
# Return the sentence.

# Step 3: Create the main function

# Create a function named main.
# Print a message explaining the program’s purpose.
# Ask the user for the desired sentence length.
# Validate the user input:
# Check if it is an integer.
# Check if it is between 2 and 20 (inclusive).
# If the input is invalid, print an error message and exit.
# If the input is valid, call get_random_sentence with the length and print the generated sentence.

import os
import random


def get_words_from_file(file_path):
    words_list = []
    with open(file_path, "r") as file:
        for line in file:
            words_list.append(line.rstrip("\n"))

    return words_list


def get_random_sentence(sentence_length: int):
    words_list = get_words_from_file(file_path)
    random_sentence = " ".join(random.choices(words_list, k=sentence_length)).lower()

    return random_sentence


def main():
    print(
        "The program opens a file consisting words, creates a list of those words, and builds a sentence made of random picked words."
    )

    try:
        length = int(
            input(
                "Enter an integer between 2 and 20. This will be the length of the sentence: "
            )
        )
    except ValueError:
        print("Input wasn't a valid integer. Existing...")

        return

    if not (2 <= length <= 20):
        print("Integer wasn't between 2 and 20. Existing...")

        return

    random_sentence = get_random_sentence(length)

    print(random_sentence)


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "words.txt")

main()

# 🌟 Exercise 2: Working with JSON
# Goal: Access a nested key in a JSON string, add a new key, and save the modified JSON to a file.

# Key Python Topics:

# JSON parsing (json.loads())
# JSON serialization (json.dump())
# Dictionaries
# File handling (open())

# Instructions:

# Using the follow code:

# import json
# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payable":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"

# Access the nested “salary” key.
# Add a new key “birth_date” which value is of format “YYYY-MM-DD”, to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Save the modified JSON to a file.

# Step 1: Load the JSON string

# Import the json module.
# Use json.loads() to parse the JSON string into a Python dictionary.

# Step 2: Access the nested “salary” key

# Access the “salary” key using nested dictionary access (e.g., data["company"]["employee"]["payable"]["salary"]).
# Print the value of the “salary” key.

# Step 3: Add the “birth_date” key

# Add a new key-value pair to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Replace "YYYY-MM-DD" with an actual date.

# Step 4: Save the JSON to a file

# Open a file in write mode ("w").
# Use json.dump() to write the modified dictionary to the file in JSON format.
# Use the indent parameter to make the JSON file more readable.

import json

sampleJson = """{
    "company": {"employee": {"name": "emma", "payable": {"salary": 7000, "bonus": 800}}}
}"""


def load_json(json_obj):
    return json.loads(json_obj)


def insert_birthdate(json_obj):
    json_obj["company"]["employee"]["birth_date"] = "1997-12-28"

    return json_obj


def save_json_file(json_obj):
    with open(output_path, "w") as file:
        json.dump(json_obj, file, indent=4)


sample_json = load_json(sampleJson)

print(sample_json)
print(sample_json["company"]["employee"]["payable"]["salary"])

sample_json = insert_birthdate(sample_json)
print(sample_json)

output_path = os.path.join(script_dir, "employee_data.json")
save_json_file(sample_json)
