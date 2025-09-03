# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)




# My Answer:

# It will give an error because the function 'foo' has 2 paramters set and was given 3 arguments.









# Launch School's Answer:

# The code will raise an error:

# TypeError: foo() takes 2 positional arguments,
# but 3 were given

# We've defined foo with two parameters. However, we've passed the function three arguments. This 
# is an error.
