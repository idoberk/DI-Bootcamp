# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Dunder methods (**str**, **int**, **repr**, **add**, **iadd**)
# Modules (importing and using)
# string module
# datetime module
# faker module

# 🌟 Exercise 1: Currencies
# Goal: Implement dunder methods for a Currency class to handle string representation, integer conversion, addition, and in-place addition.

# Key Python Topics:

# Dunder methods (**str**, **repr**, **int**, **add**, **iadd**)
# Type checking (isinstance())
# Raising exceptions (raise TypeError)

# Instructions:

# class Currency:
# def **init**(self, currency, amount):
# self.currency = currency
# self.amount = amount

#     #Your code starts HERE

# Using the code above, implement the relevant methods and dunder methods which will output the results below.

# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# #the comment is the expected output
# print(c1)

# # '5 dollars'

# print(int(c1))

# # 5

# print(repr(c1))

# # '5 dollars'

# print(c1 + 5)

# # 10

# print(c1 + c2)

# # 15

# print(c1)

# # 5 dollars

# c1 += 5
# print(c1)

# # 10 dollars

# c1 += c2
# print(c1)

# # 20 dollars

# print(c1 + c3)

# # TypeError: Cannot add between Currency type <dollar> and <shekel>

# #comment the print above before you run the file for next exercises (since the error will crash your file)


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __int__(self):
        return int(self.amount)

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type {self.currency} and {other.currency}."
                )

            return Currency(self.currency, self.amount + other.amount)

        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other

            return self

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type {self.currency} and {other.currency}."
                )

            self.amount += other.amount

            return self

        return NotImplemented

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (
            f"{self.amount} {self.currency + 's' if self.amount > 1 else self.currency}"
        )


c1 = Currency("dollar", 5)
c2 = Currency("dollar", 10)
c3 = Currency("shekel", 1)
c4 = Currency("shekel", 10)

# the comment is the expected output
print(c1)

# '5 dollars'

print(int(c1))

# 5

print(repr(c1))

# '5 dollars'

print(c1 + 5)

# 10

print(c1 + c2)

# 15

print(c1)

# 5 dollars

c1 += 5
print(c1)

# 10 dollars

c1 += c2
print(c1)

# 20 dollars

# print(c1 + c3)

# 🌟 Exercise 2: Import
# Goal: Create a module with a function and import it into another file.

# Instructions:

# Create a func.py file with a function that sums two numbers and prints the result. Then, import and call the function from exercise_one.py.

# Key Python Topics:

# Modules (creating and importing)
# Functions

# Step 1: Create func.py

# Create a file named func.py.
# Define a function inside that file that takes two numbers as arguments, sums them, and prints the result.

# Step 2: Create exercise_one.py

# Create a file named exercise_one.py.
# Import the function from func.py using one of the import syntaxes provided in the instructions.
# Call the imported function with two numbers.

from func import add_numbers

add_numbers(3, 6)
add_numbers(2, 1)
add_numbers(5, 7)

# 🌟 Exercise 3: String module
# Goal: Generate a random string of length 5 using the string module.

# Instructions:

# Use the string module to generate a random string of length 5, consisting of uppercase and lowercase letters only.

# Key Python Topics:

# string module
# random module
# String concatenation

# Step 1: Import the string and random modules

# Import the string and random modules.

# Step 2: Create a string of all letters

# Read about the strings methods HERE to find the best methods for this step

# Step 3: Generate a random string

# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.

import string
import random

random_string = "".join(random.choices(string.ascii_letters, k=5))

print(random_string)

# 🌟 Exercise 4: Current Date
# Goal: Create a function that displays the current date.

# Key Python Topics:

# datetime module

# Instructions:

# Use the datetime module to create a function that displays the current date.

# Step 1: Import the datetime module

# Step 2: Get the current date

# Step 3: Display the date

import datetime

today_date = datetime.date.today()
print(today_date)

# 🌟 Exercise 5: Amount of time left until January 1st
# Goal: Create a function that displays the amount of time left until January 1st.

# Key Python Topics:

# datetime module
# Time difference calculations

# Instructions:

# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module

# Step 2: Get the current date and time

# Step 3: Create a datetime object for January 1st of the next year

# Step 4: Calculate the time difference

# Step 5: Display the time difference

curr_date_time = datetime.datetime.now()
start_next_year = datetime.datetime(year=curr_date_time.year + 1, month=1, day=1)
time_left = start_next_year - curr_date_time
days = time_left.days
hours, remainder = divmod(time_left.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print(
    f"Time left until January 1st: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
)

# 🌟 Exercise 6: Birthday and minutes
# Key Python Topics:

# datetime module
# datetime.datetime.strptime() (parsing dates)
# Time difference calculations
# .total_seconds() method

# Instructions:

# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.


def minutes_lived(birthdate_str, date_format="%Y-%m-%d"):
    birthdate = datetime.datetime.strptime(birthdate_str, date_format)
    now = datetime.datetime.now()

    time_lived = now - birthdate
    total_minutes = int(time_lived.total_seconds() / 60)

    print(f"You have lived approximately {total_minutes:,} minutes.")

    return total_minutes


minutes_lived("1997-12-28")


# 🌟 Exercise 7: Faker Module
# Goal: Use the faker module to generate fake user data and store it in a list of dictionaries.
# Read more about this module HERE

# Key Python Topics:

# faker module
# Dictionaries
# Lists
# Loops

# Instructions:

# Install the faker module and use it to create a list of dictionaries, where each dictionary represents a user with fake data.

# Step 1: Install the faker module

# Step 2: Import the faker module

# Step 3: Create an empty list of users

# Step 4: Create a function to add users

# Create a function that takes the number of users to generate as an argument.
# Inside the function, use a loop to generate the specified number of users.
# For each user, create a dictionary with the keys name, address, and language_code.
# Use the faker instance to generate fake data for each key:
# name: faker.name()
# address: faker.address()
# language_code: faker.language_code()
# Append the user dictionary to the users list.
# Step 5: Call the function and print the users list

from faker import Faker

faker = Faker()

users = []


def add_users(count):
    for _ in range(count):
        user = {
            "name": faker.name(),
            "address": faker.address(),
            "language_code": faker.language_code(),
        }
        users.append(user)


add_users(5)

for user in users:
    print(user)
