# 🌟 Exercise 1: Favorite Numbers
# Key Python Topics:
#
# Sets
# Adding/removing items in a set
# Set concatenation (using union)
#
# Instructions:
#
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = set()
my_fav_numbers = {13, 17, 21, -12, 456}
my_fav_numbers.add(28)
my_fav_numbers.add(124)
my_fav_numbers.pop()

friend_fav_numbers = set()
friend_fav_numbers = {546, 23, 12, 76, 42, 21}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# 🌟 Exercise 2: Tuple
# Key Python Topics:
#
# Tuples (immutability)
#
# Instructions:
#
# Given a tuple of integers, try to add more integers to the tuple.

tuple_of_integers = (
    12,
    45,
    1,
    67,
)  # Since tuples are immutable, we can't modify and change them directly.

# 🌟 Exercise 3: List Manipulation
# Key Python Topics:
#
# Lists
# List methods: append, remove, insert, count, clear
#
# Instructions:
#
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")

print(apple_count)

basket.clear()
print(basket)

# 🌟 Exercise 4: Floats
# Key Python Topics:
#
# Lists
# Floats and integers
# Range generation
#
# Instructions:
#
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

mixed_list_of_int_float = [
    int(i * 0.5) if (i * 0.5).is_integer() else i * 0.5 for i in range(3, 11)
]
print(mixed_list_of_int_float)

# 🌟 Exercise 5: For Loop
# Key Python Topics:
#
# Loops (for)
# Range and indexing
#
# Instructions:
#
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for i in range(1, 21):
    print(f"{i}", end=", ")

print(f"\n")

for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i}", end=", ")

print(f"\n")

# 🌟 Exercise 6: While Loop
# Key Python Topics:
#
# Loops (while)
# Conditionals
#
# Instructions:
#
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop
# Example:
#
# Enter your name:1234
# give the correct name:hi
# give the correct name:Ana
# thank you

user_name_input = input("Enter your name: ")

while True:
    if user_name_input.isdigit() or len(user_name_input) < 3:
        user_name_input = input("give the correct name: ")
    else:
        print("thank you")
        break

# 🌟 Exercise 7: Favorite Fruits
# Key Python Topics:
#
# Input/output
# Strings and lists
# Conditionals
#
# Instructions:
#
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

favorite_fruits_input = input(
    "Enter your favorite fruit (if you have multiple, separate them by spaces): "
).lower()
fruits = [fruit.strip() for fruit in favorite_fruits_input.split(" ")]

fruit_name_input = input("Enter the name of any fruit: ").lower()
if fruit_name_input in fruits:
    print(f"You chose one of your favorite fruits! Enjoy")
else:
    print(f"You chose a new fruit. I hope you enjoy it!")

# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:
#
# Loops
# Lists
# String formatting
#
# Instructions:
#
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

pizza_toppings = []
pizza_price = 10
while True:
    topping_input = input("Please enter a pizza topping of your liking: ").lower()
    if topping_input in pizza_toppings:
        print(f"You already added {topping_input} to your pizza!")
    else:
        pizza_toppings.append(topping_input)
        print(f"Adding {topping_input} to your pizza.")
        pizza_price += 2.5
    keep_adding_toppings = input(
        "type 'quit' if you don't want to add any more toppings: "
    ).lower()
    if keep_adding_toppings == "quit":
        print(f"The pizza costs ${pizza_price}. Thank you!")
        break

# 🌟 Exercise 9: Cinemax Tickets
# Key Python Topics:
#
# Conditionals
# Lists
# Loops
#
# Instructions:
#
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.
#
# Bonus:
#
# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

family_member_count = int(
    input("How many family members would like to watch the movie: ")
)
movie_restricted = input("Is it a restricted movie (ages 16-21) 'y'/'n': ").lower()
is_restricted = True if movie_restricted == "y" else False
family_members_age = []
total_ticket_price = 0
for _ in range(family_member_count):
    person_age = int(input("What's your age: "))
    if is_restricted:
        if person_age >= 16 and person_age <= 21:
            family_members_age.append(person_age)
            total_ticket_price += 15
            print(f"Enjoy the movie!")
        else:
            print("Sorry. This movie is only for people in the ages between 16 and 21.")
    else:
        family_members_age.append(person_age)
        if person_age >= 0 and person_age < 3:
            print(f"Children under the age of 3 are getting a ticket for free!")
        elif person_age >= 3 and person_age < 12:
            print(f"Tickets for children in the ages between 3 and 12 cost $10")
            total_ticket_price += 10
        elif person_age >= 12:
            print(f"Tickets for people above the age of 12 cost $15")
            total_ticket_price += 15

print(f"Total ticket cost: {total_ticket_price}")
print(f"Attendees: {family_members_age}")
