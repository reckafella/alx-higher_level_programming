#!/usr/bin/python3

""" This module creates a class Rectangle that inherits properties of\
BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This class extends BaseGeometry """

    def __init__(self, width, height):
        """ Initialize the class """
        self.__width = BaseGeometry.integer_validator(self, "width", width)
        self.__height = BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """ Return the area of the rectangle """
        if isinstance(self.__width, int) and isinstance(self.__height, int):
            return (self.__width * self.__height)

    def __str__(self):
        """ Return Rectangle width and height """
        return ("[{}] {}/{}".
                format(self.__class__.__name__, self.__width, self.__height))
