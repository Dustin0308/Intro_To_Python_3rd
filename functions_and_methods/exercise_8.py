# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)




# It will raise a TypeError becasue the function requires 2 arguments and 3 are given when invoking 
# it.
