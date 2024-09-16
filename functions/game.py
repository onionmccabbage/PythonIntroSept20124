# we may choose to import other code
# careful: when we import something the ENTIRE module is executed
# import util # we now have the entire util module
# Careful: even if we import just a part from a module, the entire module is executed
from util import checkIsOdd # here we import just one function
from util import checkIsSquare

# Python will always assign a name to any module you run
if __name__ == '__main__':
    print(f'Python calls the running module {__name__}') # '__main__'
    # we can use functional programming as an architectural choice
    values = range(-99, 100) # a range of values
    odds = map(checkIsOdd, values) # we map all the values to the function
    for _ in odds:
        print(_, end=', ')
    squares = map(checkIsSquare, values)
    for _ in squares:
        print(_, end=', ')
    # in addition to 'map' we can also use 'filter'
    # filter will return just those members wherehte function gives us True
    just_odds = filter(checkIsOdd, values)
    # a filter object can be iterated (like a range object)
    for _ in just_odds:
        print(_)
    just_sq = filter(checkIsSquare, values)
    for _ in just_sq:
        print(_)