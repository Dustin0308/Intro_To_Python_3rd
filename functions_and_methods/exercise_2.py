# Take a look at this code snippet:

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# What does this program print? Why?

# The program prints 'bar'. It does this because when we invoke the function on line 8, we pass no arguments to it, so it doesn't output anything. Python moves to the next line, which is 'print(foo)' and prints the value of 'foo' which is 'bar'. 
# Since 'print(foo)' is searching the global scope (since there is no call to the function that has 'foo' shadowing the 'foo' variable on line 3), where it finds the variable 'foo' with the value of 'bar'. 
