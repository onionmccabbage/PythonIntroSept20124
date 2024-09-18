# more about positional and keyword arguments

def getPos(*args):
    '''all the positional arguments will automatically gather into a tuple we called args'''
    print(args)
    
def getKW(**kwargs):
    '''all the keyword arguments will automatically gather into a dictionary we called kwargs'''
    print(kwargs)

def getBoth():
    pass

if __name__ == '__main__':
    getPos(5,4,3 ,True, [], {}, None) # the position matters
    getKW(admin=False, age=42, x=4, w=(4,3,2)) # each argument has a keyword