# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# It will raise a SyntaxError since the second parameter has a default value, any parameter that 
# follows it must also have a default value and the third paramter in this function does not. 
