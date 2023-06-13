#!/usr/bin/python3

""" This module creates a class Square that inherits properties of\
Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This class extends Rectangle """

    def __init__(self, size):
        """ Initialize the class """
        self.__size = super().integer_validator("size", size)

    def area(self):
        """ Return the area of the rectangle """
        if isinstance(self.__size, int):
            return (self.__size * self.__size)

    def __str__(self):
        """ Return Rectangle width and height """
        return ("[{}] {}/{}".format(self.__class__.__bases__[0].__name__,
                                    self.__size, self.__size))
