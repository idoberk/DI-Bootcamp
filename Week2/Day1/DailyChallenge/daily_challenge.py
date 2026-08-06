# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Classes and Objects
# Dictionaries
# String Formatting
# Methods
# List manipulation and sorting

# Key Python Topics:

# Classes and Objects
# Dictionaries
# String Formatting
# Methods
# List manipulation (sorted())
# Conditional logic (if)
# String concatenation

# Instructions: Old MacDonald’s Farm

# You are given example code and output. Your task is to create a Farm class that produces the same output.

# Step 1: Create the Farm Class

# Create a class called Farm.
# This class will represent a farm and its animals.

# Step 2: Implement the __init__ Method

# The Farm class should have an __init__ method.
# It should take one parameter: farm_name.
# Inside __init__, create two attributes: name to store the farm’s name and animals to store the animals (initialize as an empty dictionary).

# Step 3: Implement the add_animal Method

# Create a method called add_animal.
# It should take two parameters: animal_type and count (with a default value of 1). Count is the quantity of the animal that will be added to the animal dictionary.
# The dictionary will look like this:
# {'cow': 1, 'pig':3, 'horse': 2}
# If the animal_type already exists in the animals dictionary, increment its count by count.
# If it doesn’t exist, add it to the dictionary as the key and with the given count as value.

# Step 4: Implement the get_info Method

# Create a method called get_info.
# It should return a string that displays the farm’s name, the animals and their counts, and the “E-I-E-I-0!” phrase.
# Format the output to match the provided example.
# Use string formatting to align the animal names and counts into columns.

# Step 5: Test Your Code

# Create a Farm object and call the add_animal and get_info methods.
# Verify that the output matches the provided example.

# Example:

# class Farm:
#     def __init__(self, farm_name):
#         # ... code to initialize name and animals attributes ...

#     def add_animal(self, animal_type, count):
#         # ... code to add or update animal count in animals dictionary ...

#     def get_info(self):
#         # ... code to format animal info from animals dictionary ...

# # Test the code
# macdonald = Farm("McDonald")
# macdonald.add_animal('cow', 5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# #output:
# # McDonald's farm

# # cow : 5
# # sheep : 2
# # goat : 12

# #     E-I-E-I-0!

# Bonus: Expand The Farm

# Step 6: Implement the get_animal_types Method

# Add a method called get_animal_types to the Farm class.
# This method should return a sorted list of all animal types (keys from the animals dictionary).
# Use the sorted() function to sort the list.

# Step 7: Implement the get_short_info Method

# Add a method called get_short_info to the Farm class.
# This method should return a string like “McDonald’s farm has cows, goats and sheeps.”.
# Call the get_animal_types method to get the list of animals.
# Construct the string, adding an “s” to the animal name if its count is greater than 1.
# Use string formatting to create the output.

# Step 8: upgrade the add_animal Method

# use **kwargs for passing multiple animals. The keys will be the animal name and the value will be the quantity.
# Then you can call the method this way: macdonald.add_animal('cow'= 5, 'sheep' = 2, 'goat' = 12)


class Farm:
    def __init__(self, farm_name: str):
        """
        A class to represent a farm and manage its animals.
        Initializes an empty dictionary to represent the animals and their count in the farm.

        Args:
            farm_name (str): Takes a farm name string parameter.
        """

        self.name = farm_name.strip().title()
        self.animals = {}

    def add_animal(self, **kwargs):
        """
        Adds one or more animals to the farm's animal dictionary.
        """

        for name, count in kwargs.items():
            animal = name.strip().lower()
            if animal not in self.animals:
                self.animals[animal] = count
            else:
                self.animals[animal] += count

    def get_info(self):
        """
        Builds the information about the farm.

        Returns:
            A string with the information about the farm (name, and animals)
        """

        if not self.animals:
            return f"{self.name}'s farm is empty"

        lines = [f"{self.name}'s farm"]

        max_name_length = max(len(animal) for animal in self.animals)

        for animal, count in self.animals.items():
            lines.append(f"{animal.ljust(max_name_length)} : {count}")

        lines.append(f"{''.ljust(max_name_length)}E-I-E-I-0!")

        return "\n".join(lines)

    def get_animal_types(self):
        """
        Returns an alphabetically sorted list of the animal types.
        """

        if self.animals:
            animal_types_list = self.animals.keys()

            return sorted(animal_types_list)
        print(f"{self.name}'s farm is empty")
        return

    def get_short_info(self):
        """
        Returns a string with information about the types of animals in the farm.
        """

        animals_list = self.get_animal_types()

        if animals_list is None:
            return f"{self.name}'s farm is empty"

        pluralized = []
        for animal in animals_list:
            if self.animals[animal] > 1:
                pluralized.append(animal + "s")
            else:
                pluralized.append(animal)

        if len(pluralized) == 1:
            animals_text = pluralized[0]
        else:
            animals_text = ", ".join(pluralized[:-1]) + " and " + pluralized[-1]

        return f"{self.name}'s farm has {animals_text}."


macdonald = Farm("McDonald")
macdonald.add_animal(cow=5, sheep=2, goat=12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
