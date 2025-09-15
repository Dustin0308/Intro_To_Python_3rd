# Consider the following nested collection:

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

# Write one line of code to print the activities that Cocoa enjoys.







# My Answer:

print(cats['Pete']['Cocoa']['enjoys'])      # {'sleeping', 'playing', 'eating', 'chewing'}





# Launch School's Answer:

print(cats['Pete']['Cocoa']['enjoys'])      # {'sleeping', 'playing', 'eating', 'chewing'}
