import write_text

if __name__ == '__main__':
    # here we declare avariable within this code-block scope
    s = 'this is some text \n to be persisted in a file'
    write_text.simpleWriter(s)
    p = 'more text'
    write_text.simpleWriter(p)
    # we can refer to a function without actually calling it
    print