# 1. Ask for User Input:
# 
# The string must be exactly 10 characters long.
# 2. Check the Length of the String:
# 
# If the string is less than 10 characters, print: "String not long enough."
# If the string is more than 10 characters, print: "String too long."
# If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
# 3. Print the First and Last Characters:
# 
# Once the string is validated, print the first and last characters.
# 4. Build the String Character by Character:
# 
# Using a for loop, construct and print the string character by character. Start with the first character, then the first two characters, and so on, until the entire string is printed.
# Hint: You can create a loop that goes through the string, adding one character at a time, and print it progressively.
# 
# Example:
# 
# h
# he
# hel
# hell
# hello
# hellow
# hellowo
# hellowor
# helloworl
# helloworld
# 
# 5. Bonus: Jumble the String (Optional)
# 
# As a bonus, try shuffling the characters in the string and print the newly jumbled string.
# Hint: You can use the random.shuffle function to shuffle a list of characters.

import random

def daily_challenge():
    while True:
        user_string = input("Enter a string that is exactly 10 characters long: ")
        string_len = len(user_string)

        if string_len < 10:
            print("String not long enough.")
        elif string_len > 10:
            print("String too long.")
        else:
            print("Perfect string")
            break
    
    print(f"First character: {user_string[0]}")
    print(f"Last character: {user_string[-1]}")

    built_string = ""
    for char in user_string:
        built_string += char
        print(built_string)
    
    char_list = list(user_string)
    random.shuffle(char_list)
    jumbled_string = "".join(char_list)

    print(f"Jumbled string: {jumbled_string}")

daily_challenge()