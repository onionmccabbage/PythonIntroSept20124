# we can use 'range' to generate a series of integer values
even_nums = range(0,101,2) # start, stop-before, step
print(type(even_nums)) # a range object
for i in even_nums:
    print(i, end=', ') # we may choose to override the default end-of-line when printing

# we can use a range to create a list
odd_nums = list(range(1, 100, 2)) # make a list from a range - NB these values DO exist in memory
print(odd_nums)

# we can use these with boolean checks
r = (4,5,6,88,2,9,33,42)
for _ in r: # _ is a common enough identifier for an iterable
    '''check if it is even or odd'''
    if _ in even_nums:
        print(f'{_} is even')
    elif _ in odd_nums:
        print(f'{_} is odd')