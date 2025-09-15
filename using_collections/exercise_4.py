# This is a 3-part question. Consider the following dictionary:

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

# Part 1: Write some code to print Bark by accessing the element associated with the key Dog.

# Part 2: Write some code to print None when you try to print the value associated with the 
#         non-existent key, Lizard.

# Part 3: Write some code to print <silence> when you try to print the value associated with the 
#         non-existent key, Lizard.



# My Answers: 

# Part 1:

print(pets['Dog'])                          # Bark



# Part 2:

print(pets.get('Lizard'))                   # None



# Part 3:

print(pets.get('Lizard', '<silence>'))      # <silence>






# Launch School's Answers:

# Part 1:

print(pets['Dog'])



# Part 2: 

print(pets.get('Lizard'))



# Part 3:

print(pets.get('Lizard', '<silence>'))




# Since the pets dictionary doesn't have a Lizard key, we need to use the dict.get method so we 
# don't get an error. In Part 2, we don't specify a default value, so get returns None. In Part 3, 
# we set <silence> as the default value.
