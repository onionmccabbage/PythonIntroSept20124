def writeBytes(b):
    '''encode some text as bytes then persist to sa byte file'''
    try:
        with open('byte_file', 'ab') as bout: # a append, w overwrite x exclusive b bytes
            bout.write(b)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    # b'' will tell Python to encode the string as bytes
    # my_bytes = b'this will be encoded as bytes'
    # writeBytes(my_bytes)
    # if you need to specify an encoding type...
    other_bytes = 'please encode this'.encode(encoding='UTF16')
    writeBytes(other_bytes)