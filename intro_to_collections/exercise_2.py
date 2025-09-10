# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?
# Note: this problem is a bit tricky.

stuff = ('hello', 'world', 'bye', 'now')







# My Answer: 

# Tuples are immutable so you cannot mutate the stuff tuple. You can create a new tuple and
# reassign it

# New tuple and reassign:

stuff = ('hello', 'world', 'goodbye', 'now')

# Or

stuff = list(stuff)
print(stuff)              # ['hello', 'world', 'bye', 'now']
stuff[2] = 'goodbye'
stuff = tuple(stuff)
print(stuff)              # ('hello', 'world', 'goodbye', 'now')





# Launch School's Answer:

# Since tuples are immutable, you can't replace 'bye' with 'goodbye'. At best, you can create a new 
# tuple and reassign it:

# Solution 1:

stuff = ('hello', 'world', 'goodbye', 'now')

# Solution 2:

stuff = stuff[0:2] + ('goodbye', stuff[3])

# Solution 3:

stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)

# Solution 1 creates an entirely new tuple with the changed value. That's not quite in the spirit 
# of what we're asking. It would also be tedious if the tuple contained more than a few elements.

# Solution 2 is a little closer to being in the proper spirit. This one concatenates a slice of the 
# original tuple combined with a new tuple that includes 'goodbye' and 'now' (from stuff[3]). 
# However, that code is difficult to read. Furthermore, the slicing and indexing is a sure-fire way 
# to get an off-by-one error. For example, if you wrote stuff[0:1] instead of stuff[0:2], the 
# result would be missing 'world'.

# Solution 3 is as close as we can get to the spirit of the problem. Here, we convert the original 
# tuple to a list and reassign the element to the new value. Finally, we transform the list into a 
# new tuple. This approach still creates an entirely new tuple. However, it avoids the problem of 
# re-entering a long list of members, is cleaner than slicing and indexing, and is much easier to 
# read.
