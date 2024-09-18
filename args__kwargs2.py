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

if __name__ == '__main__':
    getPos(5,4,3 ,True, [], {}, None) # the position matters
    getKW(admin=False, age=42, x=4, w=(4,3,2)) # each argument has a keyword
    getBoth(True, [4,3,2], {'n':'Ethel'}, 4,3,2,'Working', x=3, y=4, temp=59)