# here we extend an exception to make our own exception class

class NameError(BaseException):
    '''raise an exception related to a name error'''
    def __init__(self, msg):
        super().__init__()
        self.msg = msg # no need to validate unless we want to

if __name__ == '__main__':
    e = NameError('problem')
    raise e