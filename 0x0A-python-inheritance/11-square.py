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
        """ Return the area of the square """
        if isinstance(self.__size, int):
            return (self.__size * self.__size)

    def __str__(self):
        """ Return the size of each side of the Square """
        return ("[{}] {}/{}".format(self.__class__.__name__,
                                    self.__size, self.__size))
