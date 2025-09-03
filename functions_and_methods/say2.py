# Create a new file named say2.py with the following code:

# print('hello')
# print('hi')
# print('how do you do')
# print('Quite all right')






# Now, let's update say2.py as follows:

def say(text):
    print(text)

say('hello')
say('hi')
say('how do you do')
say('Quite all right')

# At first glance, this program seems silly. It doesn't reduce the amount of code. In fact, it adds 
# more. Also, the say function doesn't provide any functionality that print doesn't already offer. 
# However, there is a benefit here. We've extracted the logic for displaying text in a way that 
# makes our program more flexible. If we need to change the output style, we can change it in one 
# place: the say function. We don't have to change any other code to get the updated behavior.






# As mentioned earlier, one benefit that functions give us is the ability to make changes in one 
# location. Suppose we want to add a ==> to the beginning of every line that say outputs. All we h
# ave to do is change one line of code -- we don't have to change the function invocations:

def say(text):
    print('==> ' + text)

say('hello')        # ==> hello
say('hi')           # ==> hi
say('how are you')  # ==> how are you
say("I'm fine")     # ==> I'm fine





# It's sometimes helpful to invoke a function without some of its arguments. You can do that by 
# providing default values for the function's parameters. Let's update say to use a default value 
# when the caller omits the argument.

def say(text='hello'):
    print(text + '!')

say('Howdy') # Howdy!
say()        # hello!
