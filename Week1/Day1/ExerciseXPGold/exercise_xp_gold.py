# Exercise 1

print(f"Hello world\n" * 4 + "I love python\n" * 4)

# Exercise 2

user_input = int(input("Please input a number between 1 to 12: "))

if user_input in (3, 4, 5):
    print("Spring")
elif user_input in (6, 7, 8):
    print("Summer")
elif user_input in (9, 10, 11):
    print("Autumn")
elif user_input in (12, 1, 2):
    print("Winter")