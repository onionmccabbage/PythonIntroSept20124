def makeInt(x):
    '''If possible, convert x into an integer'''
    # to be robust, first convert to a float then to an int
    try:
        i = int(float(x)) # here we attempt type conversion
        return i # when we reach a return statement, the function will end
    except ValueError as err:
        return err # if there is a problem we return the string of the excetion
    print('this never happens')

# we can ask the user to enter a value
n = input('Please enter your age: ') # user input is ALWAYS a string
print(f'user entered: {n} which is {type(n)}')
# use our function
age = makeInt(n) 
print( age )

# we may check if values exist within a range
# range(start, stop-before, step)
if age in range(0,13): # the range object lets us easily handle a range of values
    print(f'{age} is too young')
elif age in range(13, 18):
    print(f'{age} needs parental permission')
elif age in range(18, 65):
    print(f'{age} is acceptable here')
else:
    print(f'by {age} you should know better')