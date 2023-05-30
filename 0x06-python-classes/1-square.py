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
    def __init__(self, size):
        """
        The __init__ method

        Args:
            size (int): size of a single side of a square

        Attributes:
            size (int): size of a single side of a square
        """
        self._size = size
