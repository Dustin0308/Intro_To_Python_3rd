# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')





# It doesn't print anything. 'return' on line 5 terminates the function before it can print anything.
