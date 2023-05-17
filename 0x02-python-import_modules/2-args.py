#!/usr/bin/python3
import sys

if __name__ == '__main__':
    num_args = len(sys.argv)

    if (num_args == 1):
        print("{:d} arguments.".format(num_args - 1))
    else:
        if (num_args == 2):
            print("{:d} argument:".format(num_args - 1))
            for i in range(num_args):
                if i > 0:
                    print("{:d}: {}".format(i, sys.argv[i]))

        elif (num_args > 2):
            print("{:d} arguments:".format(num_args - 1))
            for i in range(num_args):
                if i > 0:
                    print("{:d}: {}".format(i, sys.argv[i]))
