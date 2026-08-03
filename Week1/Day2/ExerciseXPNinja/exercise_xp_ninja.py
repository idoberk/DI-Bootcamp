# Exercise 1: Formula
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:
#
# 18,22,24

"""user_input = input("Enter a sequence of comma-separated numbers: ")
d_values = [int(num.strip()) for num in user_input.split(",")]
c, h = 50, 30
results = []
for d in d_values:
    value = (2 * c * d) / h
    q = value**0.5
    results.append(int(q))

print(results)"""

# Exercise 2 : List of integers
# Instructions
# Given a list of 10 integers to analyze. For example:
#
#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
#
#
# 1. Store the list of numbers in a variable.
#
# 2. Print the following information:
# a. The list of numbers – printed in a single line
# b. The list of numbers – sorted in descending order (largest to smallest)
# c. The sum of all the numbers
#
# 3. A list containing the first and the last numbers.
#
# 4. A list of all the numbers greater than 50.
#
# 5. A list of all the numbers smaller than 10.
#
# 6. A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
#
# 7. The numbers without any duplicates – also print how many numbers are in the new list.
#
# 8. The average of all the numbers.
#
# 9. The largest number.
#
# 10.The smallest number.
#
# 11. Bonus: Find the sum, average, largest and smallest number without using built in functions.
#
# 12. Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
#
# 13. Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
#
# 14. Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
#
# 15. Bonus: Will the code work when the number of random numbers is not equal to 10?

"""import random

list_of_int = [random.randint(-100, 100) for _ in range(random.randint(50, 75))]

for i in list_of_int:
    print(i, end=", ")

print(f"\n{sorted(list_of_int, reverse = True)}")

sum_of_list = sum(list_of_int)
print(f"sum: {sum_of_list}")

first_last_num = [list_of_int[0], list_of_int[-1]]
print(first_last_num)

greater_than_fifty = [num for num in list_of_int if num > 50]
print(greater_than_fifty)

less_than_ten = [num for num in list_of_int if num < 10]
print(less_than_ten)

squared_nums = [num**2 for num in list_of_int]
print(squared_nums)

unique_num_list = []
for num in list_of_int:
    if num not in unique_num_list:
        unique_num_list.append(num)
print(f"{unique_num_list}, length: {len(unique_num_list)}")

print(f"avg: {sum(list_of_int) / len(list_of_int)}")

print(f"max: {max(list_of_int)}")

print(f"min: {min(list_of_int)}")

avg, list_len, total, largest, smallest = 0, 0, 0, list_of_int[0], list_of_int[0]
for i in range(len(list_of_int)):
    if list_of_int[i] > largest:
        largest = list_of_int[i]
    if list_of_int[i] < smallest:
        smallest = list_of_int[i]
    total += list_of_int[i]
    list_len += 1

avg = total / list_len
print(
    f"avg: {avg}, sum: {total}, largest number: {largest}, smallest number: {smallest}"
)"""

# Exercise 3: Working on a paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

paragraph = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque maximus elit ac lacinia viverra. Cras diam quam, condimentum a ante nec, ultrices egestas nulla. Etiam vitae efficitur nibh, sed luctus tellus. Quisque vestibulum id neque non imperdiet. Maecenas sed ligula eu purus viverra facilisis at eget dui. In elit ipsum, maximus eget gravida vitae, dictum ac neque. Sed semper elementum tempor. In quam mi, mattis nec purus non, eleifend ornare diam. Integer in lectus gravida, tincidunt ipsum ac, tempor mauris. Integer id justo tellus. Nullam ut mi ut purus pellentesque tincidunt. Etiam ipsum orci, ultricies semper ipsum ut, vehicula mattis leo. Suspendisse feugiat nunc quis ipsum suscipit aliquam. Donec vestibulum scelerisque nibh, ac finibus sem congue ac. Phasellus facilisis erat ante, nec ultricies ex varius sit amet."""

sentence_enders = ".?!"
punctuations = ".?,\"'"
paragraph_len = len(paragraph)
words = []
sentence_count = 0
word_count = 0
unique_word_count = 0
non_whitespace_count = 0
avg_words_per_sentence = 0
non_unique_word_count = 0
curr_word = ""
sentence_has_content = False

for char in paragraph:
    if not char.isspace():
        non_whitespace_count += 1
    if char in sentence_enders:
        if sentence_has_content:
            sentence_count += 1
            sentence_has_content = False
    elif not char.isspace():
        sentence_has_content = True

    if char.isspace() or char in sentence_enders:
        if curr_word:
            words.append(curr_word)
            unique_word_count += 1
            curr_word = ""
    else:
        curr_word += char

if curr_word:
    words.append(curr_word)
    unique_word_count += 1

word_count = len(words)
avg_words_per_sentence = word_count / sentence_count
non_unique_word_count = word_count - unique_word_count

print(f"The paragraph has {paragraph_len} characters.")
print(f"the paragraph contains {sentence_count} sentences.")
print(f"the paragraph contains {word_count} words.")
print(f"the paragraph contains {unique_word_count} unique words.")
print(f"the paragraph contains {non_whitespace_count} non-whitespace characters.")
print(
    f"the paragraph contains {avg_words_per_sentence} words in average per sentence in the paragraph."
)
print(f"the paragraph contains {non_unique_word_count} non-unique words.")

# Exercise 4 : Frequency Of The Words
# Instructions
# Write a program that prints the frequency of the words from the input.
#
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#
# Then, the output should be:
#
#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1

sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

words = sentence.split(" ")
unique_words = set(words)

freq_list = []
for word in unique_words:
    count = words.count(word)
    freq_list.append((word, count))
freq_list.sort()

for word, count in freq_list:
    print(f"{word} : {count}")
