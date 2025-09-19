# Looping over a dictionary (iterates over dict keys by default)
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)

# Output:
# a
# b
# c


# If you want the values or pairs, you can request them with the values or items methods.
# Looping over a dictionary's values
my_dict = {'a': 1, 'b': 2, 'c': 3}
for value in my_dict.values():
    print(value)
    
# Output:
# 1
# 2
# 3



# Looping over a dictionary's key/value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
for item in my_dict.items():
    print(item)

# Output:
# ('a', 1)
# ('b', 2)
# ('c', 3)



# Using 'tuple unpacking'
# Looping over a dictionary's key/value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
for (key, value) in my_dict.items():
    print(f'{key} = {value}')

# Output:
# a = 1
# b = 2
# c = 3

# By the way: you don't need the parentheses around key, value. The following code works and is 
# more Pythonic:
# Looping over a dictionary's key/value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(f'{key} = {value}')
    