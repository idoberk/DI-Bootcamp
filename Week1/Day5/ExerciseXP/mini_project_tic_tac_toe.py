# Goal: Create a Tic Tac Toe game in Python where two players can play against each other.
#
# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Conditionals (if, elif, else)
# Loops (for, while)
# Functions
# List manipulation
# User input
#
# Key Python Topics:
#
# Lists (2D lists)
# Loops (while)
# Conditional statements (if, elif, else)
# Functions
# User input (input())
# String formatting
#
# 🛠️ What you will create
# A command-line Tic Tac Toe game that allows two players to take turns marking a 3x3 grid.
#
# Instructions:
# Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares with their symbol (‘O’ or ‘X’). The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins. If all squares are filled and no player has three in a row, the game is a tie.
#
# Step 1: Representing the Game Board
#
# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).
#
# Step 2: Displaying the Game Board
#
# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.
#
# Step 3: Getting Player Input
#
# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.
#
# Step 4: Checking for a Winner
#
# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.
#
# Step 5: Checking for a Tie
#
# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.
#
# Step 6: The Main Game Loop
#
# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).
#
# Tips:
#
# Consider creating helper functions to break down the logic into smaller, manageable parts.
# Follow the single responsibility principle: each function should do one thing and do it well.
# Think about how to switch between players.
# Think about how you will store the player’s symbol.


def get_valid_move(prompt: str):
    """Repeatedly ask for a player move until it's valid."""
    value = None

    while value is None:
        try:
            value = int(input(prompt))

            if value < 1 or value > 3:
                print("Please enter a number between 1 and 3.")
                value = None
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return value - 1


def initialize_game_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(game_board):
    grid_lines = []

    print("TIC TAC TOE")

    for i, row in enumerate(game_board):
        grid_lines.append(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < len(game_board) - 1:
            grid_lines.append("-" * len(grid_lines[0]))

    width = max(len(line) for line in grid_lines)
    border = "*" * (width + 4)

    print(border)

    for line in grid_lines:
        print(f"* {line.ljust(width)} *")

    print(f"{border}\n")


def player_input(board, player):
    print(f"Player {player}'s turn...\n")
    while True:
        row = get_valid_move("Enter row: ")
        col = get_valid_move("Enter column: ")

        if board[row][col] == " ":
            return row, col

        print(
            f"({row + 1}, {col + 1}) is already taken. Please choose a different cell."
        )


def switch_player(current_player):
    return "O" if current_player == "X" else "X"


def check_win(board, player):
    size = len(board)

    for row in board:
        row_win = True
        for cell in row:
            if cell != player:
                row_win = False
                break
        if row_win:
            return True

    for col in range(size):
        col_win = True
        for row in range(size):
            if board[row][col] != player:
                col_win = False
                break
        if col_win:
            return True

    diag_win = True
    for i in range(size):
        if board[i][i] != player:
            diag_win = False
            break
    if diag_win:
        return True

    anti_diag_win = True
    for i in range(size):
        if board[i][size - i - 1] != player:
            anti_diag_win = False
            break
    if anti_diag_win:
        return True

    return False


def check_tie(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False

    if check_win(board, "X") or check_win(board, "O"):
        return False

    return True


def play():
    game_board = initialize_game_board()
    current_player = "X"
    winner = None
    is_tie = False

    while winner is None and not is_tie:
        display_board(game_board)
        row, col = player_input(game_board, current_player)
        game_board[row][col] = current_player

        if check_win(game_board, current_player):
            winner = current_player
        elif check_tie(game_board):
            is_tie = True
        else:
            current_player = switch_player(current_player)

    display_board(game_board)

    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")


play()
