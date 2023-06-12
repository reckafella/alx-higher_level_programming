#!/usr/bin/python3

""" Module contains function that checks if an object is a type of a
specified class """


def is_same_class(obj, a_class):
    """
    Return True if obj is a type of a_class. False, otherwise.

    Args:
        obj: an object
        a_class: Python class
    """
    return (type(obj) == a_class)
