# more about positional and keyword arguments

def getPos(*args): # the * will ensure any arguments gather into 'args'
    '''all the positional arguments will automatically gather into a tuple we called args'''
    print(args)
    
def getKW(**kwargs): # the ** wil ensure any keyword argments are gathered into 'kwargs'
    '''all the keyword arguments will automatically gather into a dictionary we called kwargs'''
    print(kwargs)

def getBoth(*args, **kwargs): # NG positional arguments MUST come before keyword arguments
    print(args)
    print(kwargs)

# in Python you may only declare a function once (there is no overloading)
def myFn(*args):
    '''if no arguments are passed, just say hello
    if one argument is passed, return it directly
    for two arguemtns, try to add them together
    for any more than two argument, return them all as a list'''
    if len(args) == 0:
        return 'Hello'
    if len(args)==1:
        return args[0]
    if len(args) == 2:
        try:
            result = args[0]+args[1]
            return result
        except:
            return 'did not work'
    return list(args) # convert the tuple to a list

def moreStuff(x, y, z, a=1, b=True, c=[], *kwargs):
    pass
def yeteStuff(x, y, z, *args, **kwargs):
    pass



if __name__ == '__main__':
    getPos(5,4,3 ,True, [], {}, None) # the position matters
    getKW(admin=False, age=42, x=4, w=(4,3,2)) # each argument has a keyword
    getBoth(True, [4,3,2], {'n':'Ethel'}, 4,3,2,'Working', x=3, y=4, temp=59)
    print(myFn())
    print(myFn('wow'))
    print(myFn('one', 'two'))
    print(myFn(6,6,3,3,7,9,6,9,3))