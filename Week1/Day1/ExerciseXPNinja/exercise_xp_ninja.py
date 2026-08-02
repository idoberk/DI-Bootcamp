# Exercise 4

my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(len(my_text))

# Exercise 5

trying_flag = True

while trying_flag:
    user_input = input("Enter the longest sentence you can without using the character 'A': ")
    curr_longest_input = 0

    if 'A' not in user_input:
        input_len = len(user_input)
        if input_len > curr_longest_input:
            curr_longest_input = input_len
            print(f"Congratulations! The sentence '{user_input}' is {input_len} characters long without using the character 'A'.")
    
    keep_playing = input("Would you like to try again? Y / N: ")

    if keep_playing in ('n', 'N'):
        trying_flag = False
        print("Goodbye.")

