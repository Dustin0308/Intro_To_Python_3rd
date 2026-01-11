# In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

def multiply(left, right):                                      
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Function Names
# multiply on line 3 and 11
# get_num on line 6, 9, & 10
# float (built-in) on line 7
# input (built-in) on line 7
# print (built-in) on line 12

# Parameters:
# left and right on lines 3 & 4
# prompt on lines 6 & 7
