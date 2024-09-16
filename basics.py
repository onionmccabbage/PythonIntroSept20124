# this is a comment in Python
# Every Python file is a 'module'
# identifiers and basic data types
a = 1 # here is an integer
b = 7.3 # here we have a float
# Python will infer the data type - Python is loosely typed
print(a, type(a), b, type(b))
# we may declare a variable to another value
a = 3.5
print(a, type(a))
# maths
print(a+b, a-b, a*b, a/b)
print(b**a) # ** means raise to the power of
# some other useful mathematical operators
a = 2
b = 7
print(b//a, b%a) # // means modulo division (integer division). % is remainder

# we also have...
c = True # careful True, False, None have initial capital letter
d = False
e = None

# collection data-types
# string, tuple, list, dictionary
# a string is an immutable indexed collection of characters
s = 'hello and welcome to Python'
print(s, print(type(s)))
# All indexed collections can be sliced
print( s[0] ) # member zero of the string 
print( s[4] ) # 'o'
# s[0] = 'H' # this will fail - we are not allowed to change parts of a string
# we can of course assign a variable to adiferent string
s = 'Hello and welcome to Python' # s now points to a different memory location
# we can use slicing to grab any sub-section of an indexed collection
print( s[0:7] ) # [start:stop-before]
# mini challenge - just find the word 'welcome'
print( s[10:17] )