#!/usr/bin/python3

"""
The module contains a function that prints My name is <first name> <last name>
Prototype: def say_my_name(first_name, last_name=""):
"""


def say_my_name(first_name, last_name=""):
    """
    Print the string: My name is <first_name> <last_name>
    Args:
        first_name: string
        last_name: string
    """
    if first_name is None:
        raise TypeError("say_my_name() missing 1 required positional\
                        argument: 'first_name'")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
