# Let's write a program that asks for two numbers from the user, adds them, and then displays the 
# result. Put the following code in a new file called sum_numbers.py and then run it:

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = number1 + number2

print(f'The numbers {number1} and {number2} '
      f'add to {sum}')

# 23

# If you want to add two variables arithmetically, both must have a numeric data type.

# As we learned earlier, we can convert (coerce) strings to numbers with the int() or float() 
# function. Update line 3 from sum_numbers.py to match this code:

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = float(number1) + float(number2)

print(f'The numbers {number1} and {number2} add to {sum}')

# 5
