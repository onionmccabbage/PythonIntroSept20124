def simpleWriter(n): # we receive an argument incoming as local variables
    '''Here we will use print to output to a file'''
    try:
        # we need a file access object - Python will ask the OS to open or create the file
        fout = open('mytext.txt', 'at') # at means append text.
        # fout = open('mytext.txt', 'wt') # wt means overwite text.
        # fout = open('mytext.txt', 'xt') # xt means exlusive access to write text
        # wibbly = open('otherfile.rar','rb')
        print(n, file=fout) # tell the print statement to send output to our file access object
        fout.close() # tidy up when done! Make the object available for garbage collection
        # wibbly.close()
    except FileExistsError as err:
        print(err)

def elegantWriter(d):
    '''we can elegently close resourcces when they are no longer needed'''
    try:
        with open('log.txt', 'at') as fout: # with will let us open a file access object and auto close when done
            # remember: print() will ALWAYS add a default new line
            # write does NOT add a new line by default
            fout.write(f'{d}\n') # write will write our text to the file access object

    except Exception as err:
        print(err)

if __name__ == '__main__':
    # here we declare avariable within this code-block scope
    s = 'this is some text \n to be persisted in a file'
    simpleWriter(s)
    p = 'more text'
    simpleWriter(p)
    # we can refer to a function without actually calling it
    print
    # exercise the elegant output routine
    elegantWriter('simple text line ')