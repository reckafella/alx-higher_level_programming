#!/usr/bin/python3

"""
This module define a class Square which is used to handle the
the calculation of area of a square.
"""


class Square:
    """
    A class that defines a square.

    Args:
        size (int): size of a single side of a square

    Attributes:
        size (int): size of a single side of a square
    """
    def __init__(self, size=0):
        """
        The __init__ method

        Args:
            size (int): size of a single side of a square

        Attributes:
            size (int): size of a single side of a square
        """

        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        A method that returns the current square area
        """
        return (self.__size ** 2)
