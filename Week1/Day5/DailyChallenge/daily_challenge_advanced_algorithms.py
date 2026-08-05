# What You will learn :
# Python Basics
# Conditionals
# Loops
# Functions
#
# Instructions
# Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.
#
# import random
#
# list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
#
# target_number = 3728
#
# Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number
#
# For example
#
# 1000 and 2728 sums to the target_number 3728
# 1864 and 1864 sums to the target_number 3728

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number = 3728


def find_pairs_with_sum(list_of_numbers: list, target_sum: int):
    seen = set()
    pairs = set()

    for num in list_of_numbers:
        complement = target_sum - num
        if complement in seen:
            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        seen.add(num)

    return pairs


pairs = find_pairs_with_sum(list_of_numbers, target_number)

for pair in pairs:
    print(f"{pair[0]} and {pair[1]} sums to the target_number {target_number}")
