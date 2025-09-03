# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')



# My Answer:

# It will give an Error because there are two paramters set to the function 'foo' but only one
# argument is given when invoking it.







 


# Launch School's Answer:

# The code will raise an error:

# TypeError: foo() missing 1 required positional
# argument: 'qux'

# We've defined foo with two parameters. However, we've only passed it one argument. This is an 
# error.
