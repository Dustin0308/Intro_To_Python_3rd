# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29


# On the first call to print, they took a slice before calling 'rfind' so the method will return
# the index of the search string in that slice, not from the beginning of the string. The slice 
# given was from index 21 through index 35. That returns a string 'for the fjords', rfind then
# returns 8, which is the index of the rightmost instance of 'f'.  

# On the second call to print, calling 'rfind' before the slice, searches the whole string and
# then finds the rightmost occurence of 'f' within that slice of 21 and 35, which occurs at index 29.
 