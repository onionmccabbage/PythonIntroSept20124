# in python there are two ways to pass arguments to a function

# a function which receives normal positional arguments
def fnA(x, y, z):
    '''positional aguments x, y and z will be gathered together into a tuple'''
    return (x, y, z)

# a function which has keyword arguments (order does not matter)
def fnB(y=3, x=7, z=9): # these arguments have default values
    '''keyword argument can be gathered into a dictionary'''
    d = {'x':x, 'y':y, 'z':z}
    return d

if __name__ == '__main__':
    print( fnA(4,3,2) )
    print( fnB() )
    print( fnB(z=99, y=88, x=33) )
    # ah but....
    print( fnA(z=66,y=55,x=44) ) # we may choose to pass keyword arguments even if expecting positiola arguments
    print( fnB(99, 88, 33) )

