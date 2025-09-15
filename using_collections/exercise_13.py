# Without running the following code, determine what each print statement should print.





                                            # My Answers:       # Launch School's Answers:
cats = ('Cocoa', 'Cheddar', 
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)               # True.               True.             
print('Butter' in cats)                     # False.              False (note 1).
print('Butter' in cats[3])                  # True.               True (note 2).
print('cheddar' in cats)                    # False.              False.



# Launch School's Notes:

# Note 1: "string in list" must match a list element exactly.
# Note 2: cats[3] is 'Butterscotch' and 'Butter' is in 'Butterscotch'.
