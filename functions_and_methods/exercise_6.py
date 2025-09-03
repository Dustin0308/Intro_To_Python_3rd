# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')



# My Answer

# It doesn't print anything as 'return' terminates the program before it can print anything.



# Launch School's Answer

# This code also doesn't print anything. The return on line 3 terminates the function before it can 
# print anything.
