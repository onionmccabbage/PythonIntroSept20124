def makeInt(x):
    '''If possible, convert x into an integer'''
    # to be robust, first convert to a float then to an int
    try:
        i = int(float(x)) # here we attempt type conversion
        return i # when we reach a return statement, the function will end
    except ValueError as err:
        return err # if there is a problem we return the string of the excetion
    except Exception as err:
        pass # we might do something clever here
    print('this never happens')

# we can ask the user to enter a value
age = -99
# we often use 'while' as a run loop
count = 0
while age<0: # while will continue to loop until the condition is met
    n = input('Please enter your age: ') # user input is ALWAYS a string
    count += 1 # increments by 1
    print(f'user entered: {n} which is {type(n)} (attempt {count})')
    if count == 3:
        print('no more attempts')
        break # break will quit out of a while loop (or any loop)
    # use our function
    age = makeInt(n) 
    print( age )

# the range object does NOT persist its values in memory... so it is very performant
r = range(-9999999, 9999999) # a lot of integers, but they do NOT live in memory

# we may check if values exist within a range
# range(start, stop-before, step) and it works for int only
if age in range(0,13): # the range object lets us easily handle a range of values
    # within a string format we use {} to inject dependencies
    print(f'{age} is too young')
elif age in range(13, 18):
    print(f'{age} needs parental permission')
elif age in range(18, 65):
    print(f'{age} is acceptable here')
else:
    print(f'by {age} you should know better')