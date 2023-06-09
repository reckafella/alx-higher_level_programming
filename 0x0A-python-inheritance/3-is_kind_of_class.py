#!/usr/bin/python3

""" Module contains function that checks if an object is an instance of a
specified class """


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class. False, otherwise.

    Args:
        obj: an object
        a_class: Python class
    """
    return isinstance(obj, a_class)
