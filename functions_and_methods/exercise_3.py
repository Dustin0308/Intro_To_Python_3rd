# Write a program that uses a multiply function to multiply two numbers and returns the result. 
# Ask the user to enter the two numbers, then output the numbers and result as a simple equation.


# $ python multiply.py
# Enter the first number: 3.1416
# Enter the second number: 2.7183
# 3.1416 * 2.7183 = 8.53981128



# My Answer: (My solution is different but satisfies the answer as per LSBot).

def multiply(number1, number2):
    return number1 * number2

number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))

product = multiply(number1, number2)
print(f'{number1} * {number2} = {product}')



# Launch School's Answer:

def multiply(left, right):
    return left * right

def get_number(prompt):
    entry = input(prompt)
    return float(entry)

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')
