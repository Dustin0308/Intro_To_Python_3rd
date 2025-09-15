# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29





# My Answer:

# The first line of code (linse 5) takes a slice from index 21 through index 35 which returns the 
# string 'for the fjords'. 'rfind' then retuns 8, which is the index of the rightmost occurence of 
# 'f'.

# The second line of code (line 6) does a search for the rightmost 'f' between the two indexes of
# 21 and 35. The 'f' occurs at index 29. 






# Launch School's Answer:

# Line 3 first extracts a slice from text ranging from index 21 through index 35. That returns the 
# string 'for the fjords'. rfind then returns 8, the index of the rightmost instance of an 'f'.

# On the other hand, line 4 does a search for the rightmost f between indexes 21 and 35. Since the 
# f occurs at index 29, that's what the method returns.

