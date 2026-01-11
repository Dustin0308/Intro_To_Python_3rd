# Which of the identifiers in the following program are function names? Which are method names? Which are built-in functions?

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# Function Names:
# say on line 3 & 9
# print (built-in) on line 4
# input (built-in) on lines 6 & 7
# max (built-in) on line 9

# Method Names:
# upper & lower on line 9
