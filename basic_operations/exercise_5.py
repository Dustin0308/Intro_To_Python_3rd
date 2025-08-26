# Will an error occur if you try to access a list element with an index greater than or equal to 
# the list's length? For example:

foo = ['a', 'b', 'c']
print(foo[3])      # will this result in an error?


# My Answer:

# Yes, it will give an IndexError because the call to print on foo at index 3 doesn't exist. There
# is no index 3. If you want to print c, you would have to do this: print(foo[2]). The list doesn't
# go higher than index 2. 


# Launch School's Answer: 

# Yes, an error will occur: list index out of range. When you use an index value with no 
# corresponding element, Python raises an IndexError error.
