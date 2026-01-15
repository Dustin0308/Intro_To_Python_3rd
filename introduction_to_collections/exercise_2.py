# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

# Note: this problem is a bit tricky.

new_stuff = list(stuff)
print(new_stuff)            # ['hello', 'world', 'bye', 'now']
new_stuff[2] = 'goodbye'
print(new_stuff)            # ['hello', 'world', 'goodbye', 'now']
stuff = tuple(new_stuff)
print(stuff)                # ('hello', 'world', 'goodbye', 'now')



# You can't change(mutate) a tuple, but you can use a constructor on the tuple that is indexable
# or mutable and then mutate 'bye' to 'goodbye' within that new list (as demonstrated above). You
# can then use the tuple constructor on that mutated list to create a new tuple. This still
# doesn't mutate the original tuple though.  
