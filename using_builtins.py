# here is a class that overrides the built-in equality operator
class Word:
    '''We encapsulate a string, where equality is case-insensitive'''
    def __init__(self, word):
        self.word = word # we could write validation property methods for this
    def __str__(self):
        return f'{self.word}'
    # we may choose to override any of the built-in comparison operators
    def __eq__(self, other_word):
        # every str has .lower() for force lower case (also .upper())
        return self.word.lower() == other_word.word.lower()

# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object

if __name__ == '__main__':
    # normal comparison operators work as expected
    w1 = 'hello'
    w2 = 'Hello'
    print( w1 == w2 ) # False
    # using our Word class
    word1 = Word('hello')
    word2 = Word('Hello')
    print(word1, word2)
    print(word1 == word2) # True - since we compare the lower-case version of each