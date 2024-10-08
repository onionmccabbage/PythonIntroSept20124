# use the built-in data structures for modelling until they no longer suit the purpose
# a class is useful to gather related data (like any other structure) and add functionality

# in Python everything is an object, including classes
# By convention we use CamelCase but Python doesnt care
class Weather(): # or class Weather: or class Weather(object)
    '''this class will encapsulate temperature and wind-speed'''
    __slots__ = ['__temperature', '__windspeed']
    def __init__(self, t, w): # we must provide 'self' for any class methods
        '''this initialiser will be called every time we make an instance of this class'''
        self.temperature = t # even though this looks like a property, it calls a function
        self.windspeed = w
    # we often need to validate the properties of a class
    @property # this is how we declare a property GETTER (to retrieve a property from a class)
    def temperature(self):
        return self.__temperature # leading double-underscore prevents direct access to the proeprty
    # temperature must be an in or a float
    @temperature.setter # thjis is how we declare a property SETTER (to mutate a property of a class)
    def temperature(self, new_t):
        if type(new_t) in (int, float):
            # we use name-mangling to prevent direct access to properties
            self.__temperature = new_t
        else:
            self.__temperature = 12 # set a sensible default (we could raise exception)
    # temperature must be an in or a float
    @property
    def windspeed(self): # getter
        return self.__windspeed
    @windspeed.setter # setter
    def windspeed(self, new_w):
        if type(new_w) in (int, float):
            self.__windspeed = new_w
        else:
            raise(Exception) # raise exception
    # Every object implements __str__ so we override the built-in __str__ with our own
    def __str__(self):
        '''when we override __str__ we instruct on how to print'''
        return f'Weather report: temperature {self.temperature} wind-speed {self.windspeed}'

if __name__ == '__main__':
    # we can create instances of our class
    w1 = Weather('99', 44)
    # a potential problem is we may accidentaly change properties
    w1.temperature = False
    # w1.windspeed = []
    # remember, print will ALWAYS invoke the __str__ of the object being printed
    print(w1)
    # are we able to directly access __ properties (NO!!!)
    # print( w1.__temperature )
    # oh dear - we CAN addarbitrary properties to our instances
    # ...unless we limit the __slots__
    # w1.__temperature = 'not yet' # this adds an additional arbitrary property
    # print(w1.__temperature)
