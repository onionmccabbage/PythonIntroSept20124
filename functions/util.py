# we can use a range to make a collection of calculated values
odds = [i for i in range(0, 101) if i%2 !=0]
powers = [i**2 for i in range(0,11)]
print(powers)

def checkIsOdd(n): # triple quotes are often used for DOCSTRING
    '''validate that n is an integer, 
    then return True or False depending on if it is odd'''
    # print(f'Python calls this module {__name__}')
    if type(n) == int and n%2 !=0: # an odd integer
        return True
    else:
        return False
    
def checkIsSquare(m):
    '''Here we return True if m is a square number, otherwise return False'''
    pass # this is a convenient placeholder
    # we need to check it is not a negative number
    if type(m) in (int, float) and m>0:
        if m**0.5 == int(m**0.5): # raise to power of 0.5 is same as square root
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    '''only run the following code if this module is called directly (not on import)'''
    for _ in range(0,9):
        '''exercise the code'''
        print(f'{_} is odd: {checkIsOdd(_)} is square: {checkIsSquare(_)}')
        
