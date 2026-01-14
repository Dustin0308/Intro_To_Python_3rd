# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])



# The code outputs 'Empty' because an empty list is always falsy. The else block will run instead
# of the if block because my_list on line 4 is falsy.
