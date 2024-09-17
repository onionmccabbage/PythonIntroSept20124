# By default everything not in a function is in the global scope
def doStuff():
    s = 'local' # the variable 's' exists within this scope
    print(s) 

def accessGlobal():
    global s # access the global variable 's'
    s='what scope???'
    print(s)

def otherStuff():
    print(s) # this defalts to the global scope

if __name__ == '__main__':
    s = 'here I am' # this is in the global scope
    doStuff()
    accessGlobal()
    print(s) # what does this print
    otherStuff() # accesses the global 's'