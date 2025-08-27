# Write a program named 'greeter.py' that greets 'Victor' three times. Your program should use a 
# variable and not hard code the string value 'Victor' in each greeting. Here's an example run of 
# the program:

# $ python greeter.py
# Good Morning, Victor.
# Good Afternoon, Victor.
# Good Evening, Victor.

# This information is also included in the 'greeter.py' file.

# My Answer: 

name = 'Victor'
print(f'Good Morning, {name}.')
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')


# Launch School's Answers:

# This solution uses concatenation
name = 'Victor'
print('Good Morning, ' + name + '.')
print('Good Afternoon, ' + name + '.')
print('Good Evening, ' + name + '.')

# This solution uses f-string interpolation
name = 'Victor'
print(f'Good Morning, {name}.')
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')
