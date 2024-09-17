def readText(): # in Python everything is an object, includuing functions
    '''read text back from a text file'''
    fin = open('mytext.txt', 'rt') # rt means read text (in all cases t is the default)
    t = fin.read() # read will read all the text into one string
    # t = fin.readlines() # readlines will read each line into one string, as a list of strings
    # t = fin.readline() # read a line
    fin.close()
    return t

# NB we really should use try-except here...

def elegantRead():
    '''use with to read back text'''
    with open('log.txt', 'rt') as fin: # remember: with will auto xlose the file access object
        e = fin.read() # rad the entire file
    return e

if __name__ == '__main__':
    readText # no brackets, so here we merely referthe function object (not calling it)
    result = readText() # the brackets call the function
    print(result)
    print(elegantRead())
