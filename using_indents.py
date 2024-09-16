# blocks of code are indicated by indentation
if 3>2: # the colon indicates the start of a block of code
    print('3 is bigger than 2') # this line is indented because it is part of the code block
# when the indentation ends, we are no longer within the code block

# often used to declare a function
def doMaths(x,y): # colon indicates the start of a code block
    if x>y: # here is a new code block
        print(x+y)
    elif x<y: # else if
        print(x-y)
    else:
        print(x**y)

# end of code block (because we no longer indent)
doMaths(3,2)
doMaths(-3,-2)
doMaths(3,3)