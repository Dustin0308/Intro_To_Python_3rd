# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()



# My Answer:

# It will raise an error. No argument is given when invoking the function and it expects at least
# 1 argument since there are 2 defaults set already. The first parameter has no default value so it
# expects an argument.





# Launch School's Answer:

# The code will raise an error:

# TypeError: foo() missing 1 required positional
# argument: 'first'

# Here, we've defined foo with three parameters, with the second and third parameters having 
# default values. We haven't passed the function any arguments. That's an error, though - the 
# first parameter has no default value.
