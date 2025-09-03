# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)




# My Answer:

# It will print:

# 42
# 3                 # Default value even though one argument was given
# 2                 # Default value even though one argument was given





# Launch School's Answer:

# The code will print the following:

# 42
# 3
# 2

# Here, we've defined foo with three parameters, with the second and third parameters having a 
# default value. We've passed the function one argument, so Python uses the default value for the 
# last two parameters.
