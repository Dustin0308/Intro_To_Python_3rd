def say():
    print('Output from say')

print('First')
say()
print('Last')




# It's sometimes helpful to invoke a function without some of its arguments. You can do that by 
# providing default values for the function's parameters. Let's update say to use a default value 
# when the caller omits the argument.

def say(text='hello'):
    print(text + '!')

say('Howdy') # Howdy!
say()        # hello!
