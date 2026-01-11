# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)




# It will print: 
# 42
# 3.141592
# 2.718

# The function requires 3 arguments because it has 3 parameters (even though there are default 
# arguments for the second and third parameter) and when invoking the 'foo' function, 3 arguments 
# are given. 
