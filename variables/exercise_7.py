# What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# It outputs 'Good Morning, Afternoon, and Evening' to both Victor and Nina as intended. Name is 
# written as a constant, but since constants are not actually real to Python, it is for programmers
# only to track constants, it actually runs the code as if it is a variable. 
