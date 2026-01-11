# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)





# It will print:
# 42
# 3.141592
# 2

# The 'foo' function has 3 parameters with the second and third parameters each having a default 
# value given. When the function is invoked, there are only 2 arguments given (for the first and
# second parameters). Since it has a default value for the third parameter, the arguments used to 
# invoke the function will be used for the first and second parameters and the default argument 
# will be used for the third parameter. 
