# Without running the following code, determine what each line should print.



                                                # My Answers:           Launch School's Answers:                                            
print('johnson' in 'Joe Johnson')               # False.                False.           
print('sen' not in 'Joe Johnson')               # True.                 True.
print('Joe J' in 'Joe Johnson')                 # True.                 True.
print(5 in range(5))                            # False.                False.
print(5 in range(6))                            # True.                 True.
print(5 not in range(5, 10))                    # False.                False.
print(0 in range(10, 0, -1))                    # False.                False.
print(4 in {6, 5, 4, 3, 2, 1})                  # True.                 True.
print({1, 2, 3} in {1, 2, 3})                   # False.                False.
print({3, 2} in {1, frozenset({2, 3})})         # True.                 True.




# Launch School's Explanations:

# Line 6: 'in' with strings is case sensitive.
# Line 9: 'range(5)' does not include '5'; it ranges from '0 to 4'.
# Line 12: 'range(10, 0, -1)' does not include '0'; it ranges from '10 to 1'.
# Line 14: 'in' with sets only checks whether a specific value is in the set.
# Line 15: '{3, 2}' and 'frozenset({2, 3})' are considered equal sets. 
