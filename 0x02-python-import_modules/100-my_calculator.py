#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


if __name__ == '__main__':
    args = sys.argv
    num_args = len(args)
    operators = ['+', '-', '*', '/']

    if (num_args != 4):
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        exit(1)
    else:
        if (args[2] not in operators):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if (args[2] == operators[0]):
                print("{:d} {} {:d} = {:d}".format(
                    int(args[1]),
                    args[2],
                    int(args[3]),
                    add(int(args[1]), int(args[3]))))
            elif (args[2] == operators[1]):
                print("{:d} {} {:d} = {:d}".format(
                    int(args[1]),
                    args[2],
                    int(args[3]),
                    sub(int(args[1]), int(args[3]))))
            if (args[2] == operators[2]):
                print("{:d} {} {:d} = {:d}".format(
                    int(args[1]),
                    args[2],
                    int(args[3]),
                    mul(int(args[1]), int(args[3]))))
            if (args[2] == operators[3]):
                print("{:d} {} {:d} = {:d}".format(
                    int(args[1]),
                    args[2],
                    int(args[3]),
                    div(int(args[1]), int(args[3]))))
