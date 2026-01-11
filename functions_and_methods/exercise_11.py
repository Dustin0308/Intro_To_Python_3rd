# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# It will print:
# 42
# 3
# 2


# The 'foo' function has 3 parameters with the second and third parameters each having a default 
# value given. When the function is invoked, there is only 1 argument given (for the first 
# parameter). Since it has a default value for the second and third parameters, the argument used 
# to invoke the function will be used for the first parameter and the default arguments will be used
# for the second and third parameters. 
