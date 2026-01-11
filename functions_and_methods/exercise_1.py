# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# When we run this program we get an error: "NameError: name 'foo' is not defined." Since 'foo' is created inside a function, we must call that funciton with the function name. Using 'print(foo)' doesn't do anything because 'print' searches the global scope without
# a function call, and since 'foo' is not defined, 'print' gives an error.
