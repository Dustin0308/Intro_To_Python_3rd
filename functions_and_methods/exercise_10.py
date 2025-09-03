# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)



# My Answer:

# It will print:

# 42
# 3.141592
# 2           Default value of '2' was set by the function even though no argument was given.





# Launch School's Answers:

# The code will print the following:

# 42
# 3.141592
# 2

# Here, we've defined foo with three parameters, with the second and third parameters having 
# default values. We've passed the function two arguments, so Python uses the default value for the 
# last argument.
