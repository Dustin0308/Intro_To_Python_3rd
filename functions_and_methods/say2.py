print('hello')
print('hi')
print('how do you do')
print('Quite all right')


# Notice how we've duplicated the print call several times. Instead of calling it every time we 
# want to output something, we want to have code we can call when we need to print something.

# Now, let's update say2.py as follows:

def say(text):
    print(text)

say('hello')
say('hi')
say('how do you do')
say('Quite all right')


# Suppose we want to add a ==> to the beginning of every line that say outputs. All we have to do 
# is change one line of code -- we don't have to change the function invocations:

def say(text):
    print('==> ' + text)

say('hello')        # ==> hello
say('hi')           # ==> hi
say('how are you')  # ==> how are you
say("I'm fine")     # ==> I'm fine
