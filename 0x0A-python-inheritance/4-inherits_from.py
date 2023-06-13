#!/usr/bin/python3

""" Module contains function that checks if an object's class is a subclass of\
a specified class """


def inherits_from(obj, a_class):
    """
    Return True if obj is a subclass of a_class.
    Exclude instances of the derived class
    E.g: bool() returns False, but int() returns True
    False, otherwise.

    Args:
        obj: an object
        a_class: Python class
    """
    return (issubclass(type(obj), a_class) and not type(obj) == a_class)
