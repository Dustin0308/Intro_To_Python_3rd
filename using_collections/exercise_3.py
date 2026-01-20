# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse 
# order from the original. It should also exclude the first and last members of the original. The 
# result should be the tuple (4, 3, 2).




my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.reverse()
print(my_list)                      # [5, 4, 3, 2, 1]. (Shows me where to slice for the next code).
result = tuple(my_list[1:4])        
print(result)                       # (4, 3, 2)
