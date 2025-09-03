# In the code shown below, identify all of the function names and parameters present in the code. 
# Include the line numbers for each item identified.

def multiply(left, right):                                      # Line 1
    return left * right                                         # Line 2

def get_num(prompt):                                            # Line 4
    return float(input(prompt))                                 # Line 5

first_number = get_num('Enter the first number: ')              # Line 7
second_number = get_num('Enter the second number: ')            # Line 8
product = multiply(first_number, second_number)                 # Line 9
print(f'{first_number} * {second_number} = {product}')          # Line 10



# My Answers:

# Function Names                            
# multiply - Lines 1, 9
# get_num - Lines 4, 7, 8
# float - Line 5
# input - Line 5
# print - Line 10


# Parameters
# left, right (Lines 1, 2)
# prompt (Lines 4, 5)





# Launch School's Answers (they matched my answers)

# Function names:
# multiply: defined on line 1, used on line 9.
# get_num: defined on line 4, used on lines 7 and 8.
# float: built-in function used on line 5.
# input: built-in function used on line 5.
# print: built-in function used on line 10.

# Parameters:
# left and right are defined on line 1 and then used on line 2.
# prompt is defined on line 4 and then used on line 5.

# Note that left and right are defined as parameters for the multiply function on line 1. We 
# reference those parameters on line 2, but usually speak of them as local variables instead of 
# parameters. For this exercise, it's okay if you said that left and right are present on line 2. 
# It's also okay if you omitted it.

# Likewise, prompt is defined as a parameter for the get_num function on line 4, but used as a 
# local variable on line 5.
