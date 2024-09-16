# here we explore tuple, list, dictionary
# tuple - an immutable indexed collection of any data type
t = (5, 8, 2, True)
t2 = tuple((4,3,2)) # we make a tuple from a tuple!!!
print(t, type(t))
# list - a mutable indexed collection of any data type
l = [5, 3, 8, False]
l2 = list((6,5,4,3)) # we make a list from a tuple
l.append(l2) # we may append any members we wish
l.insert(4, 'hello') # NB strings may use single or double quotes
# it is a really good idea to use try-except
try:
    l.remove(3) # locate this value and remove it from the list
except Exception as err:
    print(err)
l.pop() # pop off the top-most value
print(l, type(l))
# we may slice a list or a tuple
print(t[0:4], l[2:4])