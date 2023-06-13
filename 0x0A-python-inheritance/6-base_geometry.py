#!/usr/bin/python3

""" Module defines a class BaseGeometry with instance method: area """


class BaseGeometry:
    """ Class BaseGeometry that adds "area" instance method """
    def __init__(self):
        """ Initialize the class instance """
        pass

    def area(self):
        """ Raises an exception since method is not implemented """
        raise Exception("area() is not implemented")
