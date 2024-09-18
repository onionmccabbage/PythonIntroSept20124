# every Python object includes many intrinsic properties

class A:
    '''This is sample class to illustrate intrinsic properties'''
    pass
    def __str__(self):
        return 'nicely formatted string'
    def __repr__(self):
        return 'this is used in immediate mode python (also in Jupyter)'

if __name__ == '__main__':
    # make some instances
    x = A()
    y = A()
    print(x.__doc__) # this will print the docstring
    print(x) # this will use __str__
    print( x.__repr__() )