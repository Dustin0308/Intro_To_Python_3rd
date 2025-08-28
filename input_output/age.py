# Write a program named age.py that asks the user to enter their age, then calculates and reports 
# the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 27 years 
# old.

# How old are you? 27

# You are 27 years old.
# In 10 years, you will be 37 years old.
# In 20 years, you will be 47 years old.
# In 30 years, you will be 57 years old.
# In 40 years, you will be 67 years old.

# This solution can also be found in the 'exercise_3.py' file. 

# My solution:

age = float(input('How old are you? '))
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')

# OR 

age = int(input('How old are you? '))
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')



# Launch School's Solution:

# This solution coerces the input age when a numeric
# age is needed. This code is repetitive.

age = input('How old are you? ')
print()
print(f'You are {age} years old.')
print(f'In 10 years, you will be {int(age) + 10} years old.')
print(f'In 20 years, you will be {int(age) + 20} years old.')
print(f'In 30 years, you will be {int(age) + 30} years old.')
print(f'In 40 years, you will be {int(age) + 40} years old.')


# And

# This solution reduces the repetition by calling int
# once only.

age = int(input('How old are you? '))
print()
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')
