# Consider this basic example of a transformative 'list comprehension':

squares = [ number * number for number in range(5) ]
print(squares)      # [0, 1, 4, 9, 16]




# Doing the same thing with a 'for' loop:

squares = []
for number in range(5):
    square = number * number
    squares.append(square)

print(squares)      # [0, 1, 4, 9, 16]







# Selection example:

multiples_of_6 = [ number for number in range(20)
                   if number % 6 == 0 ]
print(multiples_of_6)      # [0, 6, 12, 18]







# This example combines selection and transformation:

even_squares = [ number * number
                 for number in range(10)
                 if number % 2 == 0 ]
print(even_squares)      # [0, 4, 16, 36, 64]





# Iterating over a dictionary:

cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

names = [ name.upper() for name in cats_colors ]
print(names)
# ['TESS', 'LEO', 'FLUFFY', 'BEN', 'KAT']
