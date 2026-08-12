# Part II - rock-paper-scissors.py

# Step 6: Implement get_user_menu_choice Function

# Create a function called get_user_menu_choice().
# Display the menu options (“Play a new game”, “Show scores”, “Quit”).
# Get the user’s choice.
# Validate the input (e.g., check if it’s one of the valid options).
# Return the user’s choice.

# Step 7: Implement print_results Function

# Create a function called print_results(results).
# Take a dictionary called results as a parameter (e.g., {"win": 2, "loss": 4, "draw": 3}).
# Print the results in a user-friendly format (e.g., “Wins: 2, Losses: 4, Draws: 3”).
# Thank the user for playing.

# Step 8: Implement main Function

# Create a function called main().
# Pepeatedly show the menu until the user chooses to exit.
# Call get_user_menu_choice() to get the user’s choice.
# If the user chooses to play a game:
# Create a Game object.
# Call the play() method of the Game object.
# Store the result of the game in a dictionary (e.g., results).
# If the user chooses to exit:
# Call print_results() to display the game summary.
# Exit the program.

# Example (Conceptual, No Direct Solution):

# # rock-paper-scissors.py
# from game import Game

# def get_user_menu_choice():
#     # ... code to display menu and get user choice ...
#     # ... code to validate user input ...
#     # ... code to return user choice ...

# def print_results(results):
#     # ... code to print results in a user-friendly way ...
#     # ... code to thank user ...

# def main():
#     # ... code to call all the related functions depending on the user's choice.

# if __name__ == "__main__":
#     main()

from game import Game


def get_user_menu_choice():
    while True:
        print("\np - Play a new game")
        print("s - Show scores")
        print("q - Quit")

        choice = input("Choose an option: ").strip().lower()

        if choice in ("p", "s", "q"):
            return choice

        print("Invalid choice. Please enter p, s, or q.")


def print_results(results: dict):
    wins = results.get("win", 0)
    losses = results.get("loss", 0)
    draws = results.get("draw", 0)

    print(f"\nFinal results - Wins: {wins}, Losses: {losses}, Draws: {draws}")
    print("Thanks for playing!")


def main():
    results = {}

    while True:
        choice = get_user_menu_choice()

        if choice == "p":
            game = Game()
            result = game.play()
            results[result] = results.get(result, 0) + 1

        elif choice == "s":
            print_results(results)

        elif choice == "q":
            print_results(results)
            break
