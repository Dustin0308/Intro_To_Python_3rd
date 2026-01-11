# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()



# It will give a TypeError because the function requires at least 1 argument and no argument is 
# given when invoking the function. 
