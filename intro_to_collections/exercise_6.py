# Assuming you have the following assignment:

pi = 3.141592

# Write some code that converts the value of pi to a string and assigns it to a variable named 
# 'str_pi.'



# My Answer:

pi = 3.141592
str_pi = str(pi)
print(str_pi)               # 3.141592





# Launch School's Answer:

# Solution 1: 

pi = 3.141592
str_pi = str(pi)

# Solution 2:

pi = 3.141592
str_pi = f'{pi}'

# Solution 1 is the preferred solution since it is slightly more readable. Solution 2 works, too. 
# However, f-strings are better suited for creating strings mixed with other text.
