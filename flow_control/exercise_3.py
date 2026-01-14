# Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)


# It will print: Product2
#                Product not found!

# The reason for this is because when the function 'bar_code_scanner' is invoked with the argument
# '113', Python searches for that case in the code where it finds it corresponds to 'Product2'. 
# When 'bar_code_scanner' is invoked with the argument 142, Python searches for that case. Product3
# has a string of '142' but the function was invoked with an interger of 142, so they are not the
# same. Since it can't find the case, it will go to the default case of 'Product not found!'.
