# Let's use input() to write a program that displays a personalized greeting message for the user 
# based on the name she provides. Create a file named personalized_greeting.py with the following 
# code:

print("What's your name?")
name = input()

print(f'Good Morning, {name}!')


# You can also use the input() function to display the prompt the user sees:

name = input("What's your name? ")

print(f'Good Morning, {name}!')



# Alternatively, we can have input() output a newline instead of a space:

name = input("What's your name?\n")

print(f'Good Morning, {name}!')
