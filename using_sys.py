import sys # sys is a really useful library - it gives system access
import os


if __name__ == '__main__':
    ''' explore sys and os '''
    print(sys.version) # which version of Python
    print(sys.platform) # what platform are we on
    sys.path.append('c:/mystuff/utils/inhere/ooohlookfoundit')
    print(sys.path) # a list of everywhere Python will look
    # we ALWAYS receive system argument variables
    # Careful: sys.argv are ALWAYS string
    for s in sys.argv: # sys.argv is a tuple of system arguments
        # sys.argv[0] is ALWAYS the current module name and path
        print(f'Argument {s} is {type(s)}')
    # NB epsilon is the smallest possible acuracy on this computer
    print(sys.float_info) # the min and max floating point values available
    print(os.environ, os.system, os.cpu_count())

# ways to terminate a running module
# break # break out of a run-loop such as while
# sys.exit() # call the Python termination routine