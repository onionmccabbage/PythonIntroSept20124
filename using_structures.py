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

# we can iterate over indexed collections
my_string = 'iterable collection'
for c in my_string:
    print(c) # NB by default the 'print' statement will always add a new-line
    if c==' ': # == check for equality
        print('thats a space')

# we may also iterate over list and tuple
for i in l: # the colon is essential
    print(i)
for _ in t: # using _ is quite common in Python
    print(_)

# When to use list or tuple:
# by default, we would use a tuple, but if we find members need to mutate, we use a list
# A tuple is very slightly more efficient than a list

# the dictionary: a non-indexed collection of key-value pairs
# NB we usually declare the keys as strings
# the values may be ANY data type, even other collections
my_dict = {'n':'Floella', 'age':42, 'auth':'admin', 'online':False}
# we may add further key-value pairs
my_dict['skills'] = ('CI', 'Kubernetes', 'Python')
print(my_dict, type(my_dict))
# we may access members of the dict
print(my_dict['n'], my_dict['skills'][2])
# we may iterate over a dictionary (even though it is NOT indexed)
for (k,v) in my_dict.items():
    # we may choose to format the printed output
    # print(k, v, type(v))
    print ( f'{k} contains {v} which is a {type(v)}' )
    # logic allows for 'or' 'and' etc.
    if type(v)==tuple or type(v)==list: # check if we have a tuple
        for _ in v:
            print(_)
