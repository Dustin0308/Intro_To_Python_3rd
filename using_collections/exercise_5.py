# Which of the following values can't be used as a key in a dict object, and why?

'cat'                                   # Can be used. Immutable.
(3, 1, 4, 1, 5, 9, 2)                   # Can be used. Immutable.                  
['a', 'b']                              # Can't be used. Mutable.
{'a': 1, 'b': 2}                        # Can't be used. Mutable.
range(5)                                # Can be used. Immutable.
{1, 4, 9, 16, 25}                       # Can't be used. Mutable.
3                                       # Can be used. Immutable.
0.0                                     # Can be used. Immutable.
frozenset({1, 4, 9, 16, 25})            # Can be used. Immutable. 





# Launch School's Answers:

# The following items can't be used as keys:

['a', 'b']
{'a': 1, 'b': 2}
{1, 4, 9, 16, 25}

# The first value is a list, the second another dict, and the last a set. Since all 3 types are 
# mutable, they can't be used as dict keys. All remaining items are immutable built-in objects; 
# they are acceptable dict keys.
