# we can use a range to make a collection of calculated values
odds = [i for i in range(0, 101) if i%2 !=0]
powers = [i**2 for i in range(0,11)]
print(powers)

def checkIsOdd(n): # triple quotes are often used for DOCSTRING
    '''validate that n is an integer, 
    then return True or False depending on if it is odd'''
    if type(n) == int and n%2 !=0: # an odd integer
        return True
    else:
        return False
    
for _ in range(0,9):
    print(f'{_} is odd: {checkIsOdd(_)}')
        
