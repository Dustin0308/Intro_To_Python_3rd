# Which of the following values can't be used as a key in a dict object, and why?

'cat'                                                                
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']
{'a': 1, 'b': 2}
range(5)
{1, 4, 9, 16, 25}
3
0.0
frozenset({1, 4, 9, 16, 25})


# These items can't be used as keys:

['a', 'b']          # List
{'a': 1, 'b': 2}    # Dict          
{1, 4, 9, 16, 25}   # Set

# All 3 types are mutable, so they can't be used as dict keys. 
