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


if __name__ == '__main__':
    # for any collection all the data members exist in memory
    t = (0,1,2,3,4,5,6,7,8,9)
    # for a range object, only the object exists in memory
    r = range(0,10) # start,stop-before,step
    # recal, we can iterate over the members yielded from a range
    for _ in r:
        print(_)
    # once we have exhausted a range, there are no more values to use
    # in addition to simple range objects we may create a generator object
    # this is called 'comprehension' - we deal with each member comprehensively
    cubes = (i**3 for i in r) # using () will make a generator (not a tuple)
    squares = [i**2 for i in r] # using [] will make a list (not a generator)
    sqroots = tuple(i**0.5 for i in r) # a tuple
    print(r, cubes, squares, sqroots)
    # a generator (like a range) can yield subsequent values
    # Also, the values yielded by a generator do NOT live in memory (they are generated as needed)
    for _ in cubes:
        print(_)
    # mini-challenge: create a generator for all multiples of 5 from -10000 to 10000
    fives = (i for i in range(-10000, 10001, 5)) # we have a generator
    print( fives.__next__() ) # yield the next value -10000
    print( fives.__next__() ) # yield the next value -9995
    print( fives.__next__() ) # yield the next value -9990
    print( fives.__next__() ) # yield the next value -9985