# here is a class that overrides the built-in equality operator
class Word:
    '''We encapsulate a string, where equality is case-insensitive'''
    def __init__(self, word):
        self.word = word # we could write validation property methods for this
    def __str__(self):
        return f'{self.word}'

if __name__ == '__main__':
    # normal comparison operators work as expected
    w1 = 'hello'
    w2 = 'Hello'
    print( w1 == w2 ) # False
    # using our Word class
    word1 = 'hello'
    word2 = 'Hello'
    print(word1, word2)