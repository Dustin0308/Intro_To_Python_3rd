# The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)



# My Answer:

# It causes an infinte loop because the counter needs to be incremented so it evenutally returns
# falsy which would terminate the loop. 



# Launch School's Answer:

# The problem occurs in the loop body. We never increment counter, so counter < 5 always returns a 
# truthy value.
