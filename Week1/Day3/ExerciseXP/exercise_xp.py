# 🌟 Exercise 1: Converting Lists into Dictionaries
# Key Python Topics:
#
# Creating dictionaries
# Zip function or dictionary comprehension
#
# Instructions
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
#
# Lists:
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# Expected Output:
#
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
merged_dict = dict(zip(keys, values))

print(merged_dict)

# 🌟 Exercise 2: Cinemax #2
# Key Python Topics:
#
# Looping through dictionaries
# Conditionals
# Calculations
#
# Instructions
# Write a program that calculates the total cost of movie tickets for a family based on their ages.
#
# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15
#
# Family Data:
#
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.
#

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total_cost = 0
for k, v in family.items():
    if v < 3:
        print(f"{k.capitalize()}'s ticket is free!")
    elif v <= 12:
        print(f"{k.capitalize()}'s ticket costs $10")
        total_cost += 10
    else:
        print(f"{k.capitalize()}'s ticket costs $15")
        total_cost += 15
print(f"Total ticket cost: ${total_cost}")

# Bonus:
#
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.


def get_ticket_price(age):
    if age < 3:
        return 0
    elif age <= 12:
        return 10
    return 15


def exercise_two():
    family = {}
    num_of_members = None

    while num_of_members is None:
        try:
            num_of_members = int(input("How many family members are there? "))
            if num_of_members <= 0:
                print(f"Please enter a positive number.")
                num_of_members = None
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for i in range(num_of_members):
        name = None

        while name is None:
            try:
                name = input(f"Enter name for family member {i + 1}: ").strip()
                if not name.isalpha():
                    print(f"Please enter a valid name")
                    name = None
            except ValueError:
                print(
                    "Invalid input. Please enter a name only consisting alphabetical characters."
                )

        age = None

        while age is None:
            try:
                age = int(input(f"How old is {name.capitalize()}? "))
                if age < 0:
                    print(f"Age cannot be a negative number.")
                    age = None
            except ValueError:
                print("Invalid input. Please enter a valid age.")

        family[name] = age

    total_cost = 0
    for name, age in family.items():
        price = get_ticket_price(age)
        total_cost += price
        print(f"{name} (age {age}): ${price}")

    print(f"\nTotal cost: ${total_cost}")


exercise_two()

# 🌟 Exercise 3: Zara
# Key Python Topics:
#
# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()
#
# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.
#
# Brand Information:
#
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green
#
# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]},
}

print(brand)

brand.update({"number_stores": 2})
print(brand)

for type in brand["type_of_clothes"]:
    print(f"Zara has {type.capitalize()} department.")

brand.update({"country_creation": "Spain"})
print(brand)

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand)

brand.pop("creation_date")
print(brand)

if "international_competitors" in brand:
    print(brand["international_competitors"][-1])

for color in brand["major_color"]["US"]:
    print(color)

dict_keys = brand.keys()
print(f"Brand has {len(dict_keys)} keys.")
print(f"Brand dictionary keys: {dict_keys}")

# Bonus:
#
# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]},
}

more_on_zara = {"creation_date": 1975, "number_stores": 7000}

brand.update(more_on_zara)
print(brand)

# 🌟 Exercise 4: Disney Characters
# Key Python Topics:
#
# Looping with indexes
# Dictionary creation
# Sorting
#
# Instructions
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
#
# Character List:
#
# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#
# Expected Results:
#
# 1. Create a dictionary that maps characters to their indices:
#
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#
# 2. Create a dictionary that maps indices to characters:
#
# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#
# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
#
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_char_to_index_dict = {}
for index, value in enumerate(users):
    disney_char_to_index_dict.update({value: index})

print(disney_char_to_index_dict)

disney_index_to_char_dict = {}
for index, value in enumerate(users):
    disney_index_to_char_dict.update({index: value})

print(disney_index_to_char_dict)

disney_sorted_chars_dict = {}
users.sort()
for index, value in enumerate(users):
    disney_sorted_chars_dict.update({value: index})

print(disney_sorted_chars_dict)
