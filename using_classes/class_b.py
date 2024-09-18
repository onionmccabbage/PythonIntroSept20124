import class_a

class Equipment(class_a.Weather): # we may inherit from any other object
    '''Equipment needs to monitor temp and wind, and control a/c '''
    def __init__(self, t, w, name):
        # we call the init method of the parent class
        super().__init__(t,w)
        self.name = name
    @property
    def name(self):
        return self.__name # remember to use name-mangling
    @name.setter
    def name(self, new_name):
        if type(new_name)== str and len(new_name)>0:
            self.__name = new_name
        else:
            raise TypeError('Name must be a non empty string')
    # we usually override __str__
    def __str__(self):
        text = super().__str__() # call the __str__ of the parent class
        text += f' name: {self.__name}'
        return text

# you may choose to inherit from ANYTHING
class MyList(list):
    '''we now have every feature of the list object'''

class MyDict(dict):
    pass

if __name__ == '__main__':
    mast = Equipment(13, 32, 'Dublin Mast')
    print(mast)