# Exercise 1: Boolean Logic
first = 'Hello World'

# This is a comment.

print("I AM A COMPUTER!")

if 1 < 2 and 4 > 2:
    print("Math is fun.")

nope = None

True and False

len("What's my length?")

"i am shouting".upper()

int("1000")

str(4) + "real"

print(3 * "cool") # coolcoolcool

# print(1 / 0) ZeroDivisionError: division by zero

print(type([])) # <class 'list'>

name = input("What's your name? ")

number = int(input("Enter any number: "))

if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

print("apple".find('l'))

print("y" in "xylophone")

print("my_string".islower())

# Exercise 2: cat's and dog's years

def cat_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

print(cat_dog_years(10))
print(cat_dog_years(1))        
print(cat_dog_years(2))