# Assume that obj already has a value of 42 when the code below starts running. Which of the 
# subsequent statements reassign the variable? Which statements mutate the value of the object 
# that obj references? Which statements do neither? If necessary, you can read the documentation.


obj = 'ABcd'                    # Reassignment.
obj.upper()                     # Neither.
obj = obj.lower()               # Reassignment.
print(len(obj))                 # Neither.
obj = list(obj)                 # Reassignment.
obj.pop()                       # Mutation. Removes last element of the list.
obj[2] = 'X'                    # Mutation. Mutates the object by changing element in list.
obj.sort()                      # Mutation. Peforms an in-place sort.
set(obj)                        # Neither.
obj = tuple(obj)                # Reassignment.
