# Refactor this code to use a regular if statement instead.

def baz():
    return ('bar' if foo() else qux())




# My Answer:

def baz():
    if foo():
        return 'bar'
    else:
        return qux()



# Launch School's Answer:

def baz():
    if foo():
        return 'bar'
    else:
        return qux()
    
# Ternaries are most useful when both result values are given by simple expressions; anything more 
# complicated than calling a function or accessing a variable or literal value can lead to 
# unreadable code. Our original code is an excellent example of using the ternary expression; the 
# refactoring merely demonstrates how the ternary works.
