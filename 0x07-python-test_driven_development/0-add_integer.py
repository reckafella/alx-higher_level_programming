#!/usr/bin/python3

"""
This module contains a function used to add two integer values
and return the result
Function: add_integer
"""


def add_integer(a, b=98):
    """
    Return the sum of integer values a and b
    Args:
        a (int): integer
        b (int): integer
    """
    if not isinstance(a, (int, float)) or type(a) == type(True):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or type(b) == type(True):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
