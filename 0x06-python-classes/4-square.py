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

    @property
    def size(self):
        """
        This method returns the current value of 'size'
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Method validates the new value of size before updating size

        Attributes:
            value (int): integer passed to the class object
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        A method that returns the current square area
        """
        return (self.__size ** 2)
