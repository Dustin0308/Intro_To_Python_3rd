# What will the following code print?

print('abc-def'.isalpha())              # False. '-' is not a letter.
print('abc_def'.isalpha())              # False. '_' is not a letter.
print('abc def'.isalpha())              # False. ' ' is not a letter.
print('abc def'.isalpha() and           
      'abc def'.isspace())              # False.
print('abc def'.isalpha() or
      'abc def'.isspace())              # False.
print('abcdef'.isalpha())               # True.
print('31415'.isdigit())                # True.
print('-31415'.isdigit())               # False. '-' is not a digit.
print('31_415'.isdigit())               # False. '_' is not a digit.
print('3.1415'.isdigit())               # False. '.' is not a digit.
print(''.isspace())                     # False. 


# I was correct with all of my answers as they match Launch School's exactly. Launch School also 
# added these comments to their solutions:

# There are two things to note above.

# Lines 4-7 (6-9 for my above code): You can't use 'and' or 'or' to determine whether a string 
# contains a mixture of different value types. The str.isXXXXX methods determine whether every 
# character in str matches a certain class of characters. Thus, a string can't be both alphabetic 
# and whitespace. It can be alphabetic or whitespace, but that doesn't work for something like 
# 'abc def'.

# Line 13 (15 for my above code): Most of the str.isXXXXX methods return False when invoked by an 
# empty string.
