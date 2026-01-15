my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:

# 1. Are the lists assigned to my_list and another_list equal?
# 2. Are the lists assigned to my_list and another_list the same object?
# 3. Are the nested lists at index 3 of my_list and another_list equal?
# 4. Are the nested lists at index 3 of my_list and another_list the same object?

# Don't write any code for this exercise.


# 1. Are the lists assigned to my_list and another_list equal? 

# Yes because they have the same value (both are lists with the same elements).

# 2. Are the lists assigned to my_list and another_list the same object?

# No. They are not the same object. Even though they are equal in value, Python recognizes them
# as two distinct objects because the list constructor creates a new object. 

# 3. Are the nested lists at index 3 of my_list and another_list equal?

# Yes they are equal because they have the same value (both are lists with the same elements). 

# 4. Are the nested lists at index 3 of my_list and another_list the same object?

# Yes the nested lists are the same object because the list constructor creates a shallow copy of 
# the iteralbe passed as the argument. 
