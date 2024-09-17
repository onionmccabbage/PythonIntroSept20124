import datetime # very useful for working with dates and times in calculations
import time

def getTimeStamp():
    '''generators look exaclty the same as normal functions
    This generator should yield a timestamp'''
    # if a generator needs ot yield endless values, we use a runloop
    while True: # this generator will only be destroyed when this module ceases to run
        now = datetime.datetime.now()
        timestamp = now.strftime('%H:%M:%S')
        yield timestamp # instead of return, a generator must yield

# mini challenge: write a generator to yield the fiftieths between 1/50 and 50/50
def fiftieths():
    n=1
    while n<51:
        yield n/50
        n+=1

# alternative
fiftiethsB = (i/50 for i in range(1,50))

if __name__ == '__main__':
    ts = getTimeStamp() # we now have an instance of our custom generator
    print( ts.__next__() ) # this wll print the exact time att which it was called
    time.sleep(5) # pause for 5 seconds
    print( ts.__next__() ) # this wll print the exact time att which it was called
    for _ in range(0, 10**3):
        print( ts.__next__() )
    # exercise the fiftieths generator
    fif = fiftieths()
    for f in fif:
        print(f)