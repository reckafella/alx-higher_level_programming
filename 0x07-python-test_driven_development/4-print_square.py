#!/usr/bin/python3

"""
Module contains a function that prints a square with the character #
"""


def print_square(size):
    """
    Print a square with the character #

    Args:
        size: int
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif (size < 0 and isinstance(size, float)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        if size > 0:
            for i in range(size):
                for j in range(size):
                    print("#", end="")
                print()
        else:
            print()
