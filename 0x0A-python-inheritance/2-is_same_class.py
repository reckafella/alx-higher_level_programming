#!/usr/bin/python3

""" Module contains function that checks if an object is an instance of a
specified class """


def is_same_class(obj, a_class):
    """
    Return True if obj is an instance of a_class. False, otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
