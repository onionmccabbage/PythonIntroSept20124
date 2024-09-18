# use the built-in data structures for modelling until they no longer suit the purpose
# a class is useful to gather related data (like any other structure) and add functionality

# in Python everything is an object, including classes
# By convention we use CamelCase but Python doesnt care
class Weather():
    '''this class will encapsulate temperature and wind-speed'''
    def __init__(self, t, w): # we must provide 'self' for any class methods
        '''this initialiser will be called every time we make an instance of this class'''
        self.t = t
        self.w = w
    # Every object implements __str__ so we override the built-in __str__ with our own
    def __str__(self):
        '''when we override __str__ we instruct on how to print'''
        return f'Weather report: temperature {self.t} wind-speed {self.w}'

if __name__ == '__main__':
    # we can create instances of our class
    w1 = Weather(12, 2)
    # remember, print will ALWAYS invoke the __str__ of the object being printed
    print(w1, w1.t, w1.w)
