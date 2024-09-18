def checkTuple(t):
    return {True:f'{t} is a tuple', False:f'{t} is not a tuple'} [type(t)==tuple]

if __name__ == '__main__':
    a = (5,4,3,2)
    b = (a, {5,4,3,3,6,8},  [], 'this is a complex tuple')
    c = (4) # not a tuple - the () simply behave as mathematical operators
    d = (4,) # tis is a one-member tuple
    # check them
    print( checkTuple(a) ) # yes
    print( checkTuple(b) ) # yes
    print( checkTuple(c) ) # no
    print( checkTuple(d) ) # yes