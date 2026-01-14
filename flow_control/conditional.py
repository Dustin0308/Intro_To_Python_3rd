value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')


# If the input value is 3, this code prints value is 3. The code doesn't print anything if the user 
# inputs any other integer.

# We can expand the if statement to include some code that runs when value is not 3: 

# value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    print('value is NOT 3')



# We can nest if statements inside an outer if. In this next example, we nest an if statement 
# inside the else block of the outer if:

value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    if value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')



# You can rewrite the previous example using an elif block:

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')



