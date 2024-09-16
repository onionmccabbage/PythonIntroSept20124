# there are very many libraries available with standard python
import random # this will import the enitre library caled 'random'
from random import randint # here we import just one function from the 'random' library

for i in range(0, 10):
    # my_int = random.randint(0,100) # a random integer between 0 and 100
    my_int = randint(0,100)
    print(my_int) # we will see 10 different random integers 0-100