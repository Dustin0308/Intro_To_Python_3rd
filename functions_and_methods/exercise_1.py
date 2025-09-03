# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
# print(foo)

# My Answer:

# The program outputs NameError: name 'foo' is not defined. The reason for this is 'set_foo' 
# returns no value. When we call 'foo' to 'print', Python looks to the global scope for the variable
# 'foo'. Since there is no variable defined there, it outputs the above error. You have to invoke
# the function to be able to see the variable defined within that function.





# Launch School's Answer: 

# The program outputs an error: NameError: name 'foo' is not defined

# Since foo is created inside a function, it isn't in scope when executing code that isn't part of 
# that function.
