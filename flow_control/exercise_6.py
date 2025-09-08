# Write a function that takes a string as an argument and returns an all-caps version of the string 
# when the string is longer than 10 characters. Otherwise, it should return the original string. 
# Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.



# My Answer:

def caps_long(string):
    if len(string) <= 10:
        return string
    else:
        return string.upper()

print(caps_long('hello world'))          # HELLO WORLD   
print(caps_long('goodbye'))              # goodbye



# Launch School's Answer (my answer works as well):

def caps_long(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string

print(caps_long("Sue Smith"))     # Sue Smith
print(caps_long("Sue Roberts"))   # SUE ROBERTS
print(caps_long("Joe Shea"))      # Joe Shea
print(caps_long("Joe Stevens"))   # JOE STEVENS
