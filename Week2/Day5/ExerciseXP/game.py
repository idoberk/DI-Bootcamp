# Part I - game.py

# Step 1: Create the Game Class

# Step 2: Implement get_user_item Method

# Create a method called get_user_item(self).
# Ask the user to select an item (rock/paper/scissors).

# Step 3: Implement get_computer_item Method

# Create a method called get_computer_item(self).
# Randomly select an item (rock/paper/scissors).
# Return the computer’s item.

# Step 4: Implement get_game_result Method

# Create a method called get_game_result(self, user_item, computer_item).
# Take user_item and computer_item as parameters.
# Determine the result of the game based on the rules of Rock Paper Scissors.
# Return “win”, “draw”, or “loss”.

# Step 5: Implement play Method

# Create a method called play(self).
# Call get_user_item() to get the user’s choice.
# Call get_computer_item() to get the computer’s choice.
# Call get_game_result() to determine the result.
# Print the outcome of the game (user’s choice, computer’s choice, result).
# Return the result (“win”, “draw”, or “loss”) as a string.

# Example (Conceptual, No Direct Solution):

# import random

# class Game:
#     def get_user_item(self):
#         # ... code to get and validate user input ...
#         # ... code to return user's choice ...

#     def get_computer_item(self):
#         # ... code to generate computer's choice ...
#         # ... code to return computer's choice ...

#     def get_game_result(self, user_item, computer_item):
#         # ... code to determine and return game result ...

#     def play(self):
#         # ... code to get user and computer choices ...
#         # ... code to determine game result ...
#         # ... code to print game outcome ...
#         # ... code to return game result ...

import random


class Game:
    OPTIONS = ["rock", "paper", "scissors"]

    def get_user_item(self):
        """
        Method to validate user input and return the input if valid.
        """
        while True:
            choice = input("Choose rock, paper, scissors: ").strip().lower()
            if choice in self.OPTIONS:
                return choice
            print("Invalid choice. Please enter rock, paper, or scissors.")

    def get_computer_item(self):
        """
        Method that returns a random option for the computer.
        """
        return random.choice(self.OPTIONS)

    def get_game_result(self, user_item: str, computer_item: str):
        """
        Method that returns the result of the game.
        """
        if user_item == computer_item:
            return "draw"

        beating = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

        if beating[user_item] == computer_item:
            return "win"

        return "loss"

    def play(self):
        """
        Method that ties up all the game together.
        """
        user_choice = self.get_user_item()
        computer_choice = self.get_computer_item()
        result = self.get_game_result(user_choice, computer_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(f"Result: {result}\n")

        return result
