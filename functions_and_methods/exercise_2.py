# Take a look at this code snippet:

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# What does this program print? Why?



# My Answer: 
# It prints 'bar' because 'foo' is defined in the global scope and is within scope of 'print(foo)'. 
# The 'foo' variable on line 6 above is in scope within that function only and shadows the 'foo'
# variable in the global scope (line 3 above). Since 'print(foo)' doesn't invoke the function,
# it doesn't look to the variable 'foo' within the function but does refer to it in the global scope.




# Launch School's Answer: 

# The program prints bar since the assignment on line 4 creates a new variable that is local to the 
# function. That is, the foo variable on line 4 shadows the foo variable on line 1, so line 4 
# doesn't change the value of foo from line 1.
