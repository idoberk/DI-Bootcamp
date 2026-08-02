# Exercise 1: Hello World

print(f"Hello world\n" * 4)

# Exercise 2: Some Math

print((99 ** 3) * 8)

# Exercise 3: What is the output?

print(5 < 3) # False
print(3 == 3) # True
print(3 == "3") # False
# print("3" > 3) # Error
print("Hello" == "hello") # False

# Exercise 4: Your computer brand

computer_brand = "Dell"
print(f"I have a {computer_brand} computer.")

# Exercise 5: Your information

name = "Ido"
age = 28
shoe_size = 43
info = f"My name is {name}, I am {age} years old, and wear {shoe_size} size shoes."
print(info)

# Exercise 6: A & B

a, b = 4, 6
if a > b:
    print("Hello World")

# Exercise 7: Odd or Even

user_input = int(input("Enter any integer you want: "))
print(f"{'Even' if user_input % 2 == 0 else 'Odd'}")

# Exercise 8: What's your name?

user_name = input("What's your name? ")
if user_name.lower() == name.lower():
    print("What a coincidence! We share the same name!")

# Exercise 9: Tall enough to ride a roller coaster

user_height = int(input("What's your height (in centimeters): "))
print(f"{'You are tall enough to ride' if user_height > 145 else 'You need to grow some more'}")