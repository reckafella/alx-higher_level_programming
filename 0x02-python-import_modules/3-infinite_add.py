#!/usr/bin/python3
import sys

if __name__ == '__main__':
    num_args = len(sys.argv)
    total = 0

    if (num_args == 1):
        print("{:d}".format(0))
    else:
        for i in range(num_args):
            if i > 0:
                total += int(sys.argv[i])
        print("{:d}".format(total))
