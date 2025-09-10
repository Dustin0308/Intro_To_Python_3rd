# Bob expects the following code to print the names in alphabetical order. Without running the 
# code, can you say whether it will? Explain your answer.

names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)





# My Answer: 

# There is no guarantee it will print in alphabetical order because it is a set. Sets maintain an 
# unordered collection of objects so they can print in random orders. 



# Launch School's Answer:

# This code probably won't print the names alphabetically. Sets, by definition, are unordered 
# collections. Thus, the order in which members are shown when printing or iterating is arbitrary. 
# Bob's code may print the names alphabetically on rare occasions, but it would do so only once 
# every 5040 times.
