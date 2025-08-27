# What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)


# My Answer:

# It will print 3 greetings to both Victor and Nina. Even though the variable 'NAME' is 
# non-idiomatic, since it is all caps (reserved for constants), Python doesn't recognize actual 
# constants. The naming conventions for constants is strictly for programmers only. Proper naming
# conventions for the variable 'NAME' should be 'name = '.


# Launch School's Answer:

# The program first greets Victor 3 times. It then greets Nina 3 times.

# Unfortunately, Python doesn't have real constants. There's no way to prevent the reassignment of 
# NAME. If this faux-constant really needs to be changed, you should use a regular variable instead:

name = 'Victor'
print('Good Morning, ' + name)
print('Good Afternoon, ' + name)
print('Good Evening, ' + name)

name = 'Nina'
print('Good Morning, ' + name)
print('Good Afternoon, ' + name)
print('Good Evening, ' + name)
