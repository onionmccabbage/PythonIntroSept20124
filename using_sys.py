import sys # sys is a really useful library - it gives system access

if __name__ == '__main__':
    ''' explore sys '''
    print(sys.version) # which version of Python
    print(sys.platform) # what platform are we on
    # we ALWAYS receive system argument variables
    # Careful: sys.argv are ALWAYS string
    for s in sys.argv: # sys.argv is a tuple of system arguments
        # sys.argv[0] is ALWAYS the current module name and path
        print(f'Argument {s} is {type(s)}')

# ways to terminate a running module
# break # break out of a run-loop such as while
# sys.exit() # call the Python termination routine