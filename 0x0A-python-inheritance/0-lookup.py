#!/usr/bin/python3

"""
This module contains a function that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object 'obj'

    Args:
        obj (object): argument
    """
    lst = dir(obj)
    return (lst)
