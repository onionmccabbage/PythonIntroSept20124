def readBytes():
    '''read a byte file'''
    try:
        with open('byte_file', 'rb') as bin: # r will read
            b = bin.read(b)
    except Exception as err:
        print(err)
    return b


if __name__ == '__main__':
    result = readBytes()
    print(result) # can we print bytes???