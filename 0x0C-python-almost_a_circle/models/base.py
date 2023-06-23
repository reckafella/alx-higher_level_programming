#!/usr/bin/python3

""" Module contains the Base class that is imported by other classes """


class Base:
    """Base class

    Attributes:
        id (int): integer value
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor used to initialize each object """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects