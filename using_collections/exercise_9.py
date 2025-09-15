# Write some code to replace the value 6 in the following nested list with 606:

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]




# My Answer: I did a step-by-step showing of my thought process to break down this problem below:

print(stuff)            # [['hello', 'world'], ['example', 'mem', None, 6, 88], [4, 8, 12]]
print(stuff[1])         # ['example', 'mem', None, 6, 88] 
print(stuff[1][3])      # 6           
stuff[1][3] = 606       # Changed value of nested list at index [1][3] from '6' to '606'.
print(stuff)            # [['hello', 'world'], ['example', 'mem', None, 606, 88], [4, 8, 12]]







# Launch School's Answer:

stuff[1][3] = 606       # Shown above in my code on line 17. 
