# Write a function, even_or_odd, that determines whether its argument is an even or odd number. 
# If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the 
# argument is always an integer.

# My answer:

def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')
        
even_or_odd(2)      # even
even_or_odd(4)      # even
even_or_odd(5)      # odd
even_or_odd(7)      # odd




# Launch School's Answers:

# Solution 1:

def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')


# Solution 2:

def even_or_odd(number):
    print('even' if number % 2 == 0 else 'odd')
    