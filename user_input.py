def makeInt(x):
    '''If possible, convert x into an integer'''
    i = int(x) # here we attempt type conversion
    return i # when we reach a return statement, the function will end
    print('this never happens')

# we can ask the user to enter a value
n = input('Please enter you name: ') # user input is ALWAYS a string
print(f'user entered: {n} which is {type(n)}')
# use our function
print( makeInt(n) )