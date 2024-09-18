import class_a
from random import randint
import time

class Equipment(class_a.Weather): # we may inherit from any other object
    '''Equipment needs to monitor temp and wind, and control a/c 
    if temp is less than 12 turn on heater, temp>28 turn on a/c'''
    __slots__ = ['__temperature', '__windspeed', '__name', '__ac', '__heater']
    def __init__(self, t, w, name):
        # we call the init method of the parent class
        super().__init__(t,w)
        self.name = name
        self.__heater = False
        self.__ac = False
    @property
    def name(self):
        return self.__name # remember to use name-mangling
    @name.setter
    def name(self, new_name):
        if type(new_name)== str and len(new_name)>0:
            self.__name = new_name
        else:
            raise TypeError('Name must be a non empty string')
    # we need  to monitor the temoperature and control heat/ a/c
    def checkTemp(self):
        '''return 'low' 'ok' or 'high' '''
        if self.temperature <12: # call the getter property method of the parent class
            return 'low'
        elif self.temperature >28:
            return 'high'
        else:
            return 'ok'
    def controlClimate(self):
        result = self.checkTemp()
        if result=='low':
            self.__heater = True
            self.__ac     = False
        elif result=='high':
            self.__heater = False
            self.__ac     = True
        else:
            self.__heater = False
            self.__ac     = False
    # we usually override __str__
    def __str__(self):
        text = super().__str__() # call the __str__ of the parent class
        text += f' name: {self.__name} Heater: {self.__heater} A/C: {self.__ac}'
        return text

# you may choose to inherit from ANYTHING
class MyList(list):
    '''we now have every feature of the list object'''

class MyDict(dict):
    pass

if __name__ == '__main__':
    mast = Equipment(13, 32, 'Dublin Mast')
    print(mast)
    # play with the temperature
    while True:
        t = randint(-99, 100)
        if t==100:
            break
        mast.temperature = t
        mast.controlClimate()
        print(mast)
