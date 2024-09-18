# unitary means singular
# binary means exactly two disctinct values
# ternary means exactly three parts
def compare(x,y):
    '''here is the python ternary operator for logic'''
    # if x<y:
    #     return f'{x} is less than {y}'
    # elif y<=x:
    #     return f'{y} is less or equal to {x}'
    return f'{x} is less than {y}' if x<y else f'{y} is less or equal to {x}'

def anotherCompare(m,n):
    '''we may also declare a ternary operator using a dict for True and False outcomes'''
    return {True:f'{m} is < {n}', False:f'{n} is <= {m}'} [m<n]

if __name__ == '__main__':
    print( compare(3,7) )
    print( compare(7,3) )
    print( compare(7,7) )
    print(anotherCompare(3,8))
    print(anotherCompare(9,3))