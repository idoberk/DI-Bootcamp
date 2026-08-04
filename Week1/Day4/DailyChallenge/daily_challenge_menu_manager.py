# Daily Challenge: Coffee Shop Menu Manager
# You were hired to help a small coffee shop manage their product menu using Python.
#
# Write a program that:
#
# 1. Stores the coffee shop menu in memory
# 2. Lets the user:
#
# Create a new item
# Read (view) all items
# Update an item’s price
# Delete an item
# Exit
# Your program must be organized with functions.
# Do not write all the logic in one giant while loop.
# You should split behavior into reusable functions.
#
# 1. Data structure
# We will represent the menu using a dictionary called menu.
#
# The key is the drink name (string)
# The value is the price (float)
# Example starting data (you MUST start with this so tests are consistent):
#
# menu = {
#     "espresso": 7.0,
#     "latte": 12.0,
#     "cappuccino": 10.0
# }
#
# 2. Required functions
# You must implement the following functions.
#
# a) show_menu(menu_dict)
# Input: the dictionary
# Output: prints all items in the format drink - price₪
# If the menu is empty, print: "The menu is empty."
# Example:
#
# Current menu:
# espresso - 7.0₪
# latte - 12.0₪
# cappuccino - 10.0₪
# This function only prints. It does not return anything.
#
# b) add_item(menu_dict)
# Ask the user for:
# drink name
# price
# Add it to the dictionary.
# If the drink already exists, print "Item already exists!" and do not change the price.
# Example interaction:
#
# Enter new drink name: mocha
# Enter price: 14
# "mocha" added!
# This function mutates the dictionary. It does not return anything.
#
# c) update_price(menu_dict)
# Ask the user which drink they want to update.
# If it exists:
# ask for the new price
# update it
# print: "Price updated!"
# If it doesn’t exist:
# print: "Item not found."
#
# d) delete_item(menu_dict)
# Ask the user which drink to remove.
# If it exists:
# delete it from the dict
# print: "Item deleted."
# Otherwise:
# print: "Item not found."
#
# e) show_options()
# Prints the main menu of actions for the user:
# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# Only prints. Doesn’t return anything.
#
# f) run_coffee_shop()
# This is the main controller of the program.
#
# Behavior:
#
# Keep running in a loop.
# Show options.
# Ask the user to choose (1-5).
# Depending on the choice, call the correct function.
#
# Rules:
#
# Invalid choice → print "Invalid choice, try again."
# Choice 5 stops the loop and prints "Goodbye!"
#
# 3. Program flow (example)
# This is what using the program might look like when it runs:
#
# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# > 1
# Current menu:
# espresso - 7.0₪
# latte - 12.0₪
# cappuccino - 10.0₪
#
# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# > 2
# Enter new drink name: mocha
# Enter price: 14
# "mocha" added!
#
# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# > 3
# Which drink do you want to update? latte
# Enter the new price: 13
# Price updated!
#
# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# > 4
# Which drink do you want to delete? espresso
# Item deleted!
#
# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# > 1
# Current menu:
# latte - 13.0₪
# cappuccino - 10.0₪
# mocha - 14.0₪
#
# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# > 5
# Goodbye!
#
# 4. Starter template (students fill in the TODOs)
# # Coffee Shop Menu Manager
#
# # Initial data
# menu = {
#     "espresso": 7.0,
#     "latte": 12.0,
#     "cappuccino": 10.0
# }
#
# def show_menu(menu_dict):
#     """Print all drinks and prices."""
#     pass
#
# def add_item(menu_dict):
#     """Add a new drink to the menu."""
#     pass
#
# def update_price(menu_dict):
#     """Change the price of an existing drink."""
#     pass
#
# def delete_item(menu_dict):
#     """Remove a drink from the menu."""
#     pass
#
# def show_options():
#     """Print the available actions."""
#     pass
#
# def run_coffee_shop():
#     """Main loop of the program."""
#     # TODO
#     # while True:
#     #   1. show_options()
#     #   2. get user choice
#     #   3. if 1 -> show_menu(menu)
#     #      if 2 -> add_item(menu)
#     #      if 3 -> update_price(menu)
#     #      if 4 -> delete_item(menu)
#     #      if 5 -> print("Goodbye!") and break
#     #      else -> "Invalid choice, try again."
#     pass
#
# # Start the program
# run_coffee_shop()
#
# 5. Extra challenges (only if they finish early)
# Ask fast students to add one or more:
#
# 1. Validation:
# Don’t allow negative prices. If the user enters -5, print "Invalid price." and don’t change anything.
#
# 2. Search function:
# Add a function search_item(menu_dict) that asks for a drink name and:
#
# prints the price if found
# else prints "Not in the menu."
# Then add it as option 6 in the menu.
# 3. Discount day:
# Add a function apply_discount(menu_dict, percent) that reduces every price by a percentage.
# Example: apply_discount(menu, 10) makes 10% off happy hour.

menu = {"espresso": 7.0, "latte": 12.0, "cappuccino": 10.0}
menu_options = [
    "Show menu",
    "Add item",
    "Update price",
    "Delete item",
    "Exit",
    "Search item",
    "Apply happy hour (10% discount)",
]


def get_valid_drink_name(prompt: str):
    """Repeatedly ask for a drink name until it's valid, then return it."""
    drink = None

    while drink is None:
        try:
            drink = input(prompt).strip().lower()

            if not drink.replace(" ", "").isalpha():
                print("Drink name can only include alphabetical characters.")
                drink = None
        except ValueError:
            print("Invalid input. Please enter a valid drink name.")

    return drink


def get_valid_price(prompt: str):
    """Repeatedly ask for a price until it's valid, then return it."""
    price = None

    while price is None:
        try:
            price = float(input(prompt))

            if price <= 0:
                print("Price cannot be a negative number.")
                price = None
        except ValueError:
            print("Invalid input. Please enter a valid price.")

    return price


def show_menu(menu_dict: dict):
    """Print all drinks and prices."""
    if not menu_dict:
        print("The menu is empty.")
        return

    print("Current menu:")
    for drink, price in menu_dict.items():
        print(f"{drink} - {price}₪")


def add_item(menu_dict: dict):
    """Add a new drink to the menu."""
    drink = get_valid_drink_name("Enter new drink name: ")

    if drink in menu_dict:
        print("Item already exists!")

    else:
        price = get_valid_price(f"Enter price: ")

        menu_dict[drink] = price
        print(f'"{drink}" added!')


def update_price(menu_dict: dict):
    """Change the price of an existing drink."""
    drink = get_valid_drink_name("What drink do you want to update? ")

    if drink not in menu_dict:
        print("Item not found.")

    else:
        price = get_valid_price(f"Enter the new price: ")

        menu_dict[drink] = price
        print(f"Price updated!")


def delete_item(menu_dict: dict):
    """Remove a drink from the menu."""
    drink = get_valid_drink_name("Which drink would you like to delete? ")

    if drink not in menu_dict:
        print("Item not found.")

    else:
        del menu_dict[drink]
        print(f"Item deleted.")


def show_options(options_list: list):
    """Print the available actions."""
    print("What would you like to do?")
    for index, option in enumerate(options_list):
        print(f"{index + 1}. {option.capitalize()}")


def search_item(menu_dict: dict):
    """Search a drink from the menu."""
    drink = get_valid_drink_name("Which drink would you like to search for? ")

    if drink not in menu_dict:
        print("Not in the menu.")

    else:
        print(f"{drink} costs {menu_dict[drink]}₪")


def apply_discount(menu_dict: dict, percent):
    """Add a discount to all the drinks in the menu by given percentage"""
    for drink, price in menu_dict.items():
        menu_dict[drink] = price - ((price * percent) / 100)


def run_coffee_shop():
    """Main loop of the program."""
    continue_operating = True

    while continue_operating:
        show_options(menu_options)
        user_choice = None

        while user_choice is None:
            try:
                user_choice = int(input(f"> "))

                if user_choice <= 0 or user_choice > len(menu_options):
                    print("Invalid choice, try again.")
                    user_choice = None
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if user_choice == 1:
            show_menu(menu)

        elif user_choice == 2:
            add_item(menu)

        elif user_choice == 3:
            update_price(menu)

        elif user_choice == 4:
            delete_item(menu)

        elif user_choice == 6:
            search_item(menu)

        elif user_choice == 7:
            apply_discount(menu, 10)

        else:
            print("Goodbye!")
            continue_operating = False


run_coffee_shop()
