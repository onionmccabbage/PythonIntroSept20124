# we may choose to import other code
# careful: when we import something the ENTIRE module is executed
# import util # we now have the entire util module
# Careful: even if we import just a part from a module, the entire module is executed
from util import checkIsOdd # here we import just one function

# Python will always assign a name to any module you run
if __name__ == '__main__':
    print(f'Python calls the running module {__name__}') # '__main__'