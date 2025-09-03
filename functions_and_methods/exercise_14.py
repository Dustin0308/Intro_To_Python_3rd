# Identify all of the identifiers on each line of the following code.

def multiply(left, right):                                  # Line 1
    return left * right                                     # Line 2

def get_num(prompt):                                        # Line 4
    return float(input(prompt))                             # Line 5

first_number = get_num('Enter the first number: ')          # Line 7
second_number = get_num('Enter the second number: ')        # Line 8
product = multiply(first_number, second_number)             # Line 9
print(f'{first_number} * {second_number} = {product}')      # Line 10



# My Answers: multiply, left, right, first_number, second_number, get_num, prompt, float, input,
#            product, print

# Line 1: multiply, left, right
# Line 2: left, right
# Line 4: get_num, prompt
# Line 5: prompt, float, input
# Line 7: first_number, get_num
# Line 8: second_number, get_num
# Line 9: product, multiply, first_number, second_number
# Line 10: first_number, second_number, product, print





# Launch School's Answers (they match my answers, I checked to be sure):

# The identifiers in this code are multiply, left, right, first_number, second_number, get_num, 
# prompt, float, input, product, and print. The following table shows where each identifier appears 
# in the code.

# Identifier	    Appears on these lines
# multiply	        1, 9
# left	            1, 2
# right	            1, 2
# first_number	    7, 9, 10
# second_number	    8, 9, 10
# get_num	        4, 7, 8
# prompt	        4, 5
# float	            5
# input	            5
# product	        9, 10
# print	            10
