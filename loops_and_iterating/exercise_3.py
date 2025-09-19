# Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a 
# for loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

# Expected Output:

# 6
# 3
# 0
# 11
# 20
# 4
# 17


# My Answers: 

# while loop

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# for loop

my_list = [6, 3, 0, 11, 20, 4, 17]

for index in my_list:
    print(index)




# Launch School's Answers:

# while loop

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    number = my_list[index]
    print(number)
    index += 1

# for loop

my_list = [6, 3, 0, 11, 20, 4, 17]

for number in my_list:
    print(number)

# Our solution using a while loop uses indexing to control iteration and to access the list 
# members. Note that we start by setting index to 0 and then iterate while index is less than the 
# list length.

# The solution using a for loop is clearly easier to understand -- we don't have to mess around 
# with indexing; we only need to iterate over the list elements.
