# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. The updated code 
# should use a for loop to display the future ages.

# Input/Output, exercise 3:

# Write a program named age.py that asks the user to enter their age, then calculates and reports 
# the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 27 years 
# old.

# How old are you? 27

# You are 27 years old.
# In 10 years, you will be 37 years old.
# In 20 years, you will be 47 years old.
# In 30 years, you will be 57 years old.
# In 40 years, you will be 67 years old.

# My Answer: (I stuggled on this, had to get help)

age = int(input('How old are you? '))
print(f'You are {age} years old.')
print()

for future in range(10, 50, 10):
    print(f'In {future} years, you will be '
          f'{age + future} years old.')
    
# Output: How old are you? 27
#         You are 27 years old.

#         In 10 years, you will be 37 years old.
#         In 20 years, you will be 47 years old.
#         In 30 years, you will be 57 years old.
#         In 40 years, you will be 67 years old.


# Launch School's Answer:

age = int(input('How old are you? '))
print(f'You are {age} years old.')
print()

for future in range(10, 50, 10):
    print(f'In {future} years, you will be '
          f'{age + future} years old.')
   