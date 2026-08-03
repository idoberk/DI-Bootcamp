# Exercise 1: Concatenate lists
# Instructions
# Write code that concatenates two lists together without using the + sign.

"""list1 = ["Apples", "Oranges", "Bananas"]
list2 = ["Tomatoes", "Peppers", "Cucumbers"]
concatenated_list = []

for item in list1:
    concatenated_list.append(item)
for item in list2:
    concatenated_list.append(item)

print(concatenated_list)"""

# Exercise 2: Range of numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

"""for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)"""

# Exercise 3: Check the index
# Instructions
# Using this variable
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
#
# Example: if input is 'Cortana' we should be printing the index 1

"""names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Please enter your name: ")

if user_name in names:
    print(names.index(user_name))"""

# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
#
# Test Data
# Input the 1st number: 25
# Input the 2nd number: 78
# Input the 3rd number: 87
#
# The greatest number is: 87

"""num_list = []
for i in range(3):
    user_input = int(input("Enter your number: "))
    num_list.append(user_input)

num_list.sort()
print(f"The greatest number is: {num_list[-1]}")"""

# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

"""alphabet_list = [chr(char) for char in range(97, 122)]
alphabet_string = ''.join(alphabet_list)

for char in alphabet_string:
    if char in ['a', 'e', 'i', 'o', 'u']:
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")"""

# Exercise 6: Words and letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

"""words = []
for i in range(7):
    words.append(input("Enter a word: ").lower())

letter = input("Enter a single character: ").lower()

for word in words:
    print(f"{word.find(letter) if letter in word else "The word '" + word + "' doesn't contain the letter " + letter}")"""

# Exercise 7: Min, Max, Sum
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.

"""one_to_million_list = [i for i in range(1, 1000001)]
print(min(one_to_million_list), max(one_to_million_list), sum(one_to_million_list))"""

# Exercise 8 : List and Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
#
# Suppose the following input is supplied to the program: 34,67,55,33,12,98
#
# Then, the output should be:
#
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

"""user_input = input("Enter a sequence of comma-separated numbers: ")
numbers = [num.strip() for num in user_input.split(',')]
numbers_list = list(numbers)
numbers_tuple = tuple(numbers)

print(numbers_list)
print(numbers_tuple)"""

# Exercise 9 : Random number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

import random

keep_playing = True
times_played = 0
times_won = 0

while keep_playing:
    user_input = int(input("Enter a number between 1 to 9 (inclusive): "))
    rand_number = random.randint(1, 9)
    if user_input == rand_number:
        times_won += 1
        print("Winner")
    else:
        print("Better luck next time")
        print(f"{rand_number}")

    times_played += 1
    user_input = input(
        f"Press any key if you would like to continue playing, or press 'q' to quit: "
    ).lower()
    if user_input == "q":
        keep_playing = False
        print(
            f"You've played {times_played} {'times' if times_played > 1 else 'time'} and won {times_won} {'times' if times_won > 1 else 'time'}"
        )
