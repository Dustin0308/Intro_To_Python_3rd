# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)



# My answer:

# It will raise an error. The function 'foo' requires at least 2 arguments 
# (first and third parameters) and only one was given. Also, once a default value is set, all 
# subsequent parameters must also have default vaules set. 





# Launch School's Answer:

# The code will raise an error:

# SyntaxError: non-default argument follows
# default argument

# Here, we've defined foo with three parameters, with the second parameter having a default value. 
# This is an error, however. Once Python sees a positional parameter with a default value, all 
# subsequent parameters must have default values.
