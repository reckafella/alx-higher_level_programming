#!/usr/bin/python3

""" This module implements a class Rectangle """


class Rectangle:
    """ This class is a representation of a rectangle.
    The class does nothing
    """
    def __init__(self, width=0, height=0):
        """
        This initializes a class object with values of height and width

        Args:
            width (int): integer value representing the width of a rectangle
            height (int): integer value representing the height of a rectangle
        """

        if (type(width) != int):
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if (type(height) != int):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """
        Retrieves the current value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width to value passed as an argument

        Args:
            value (int): integer value
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieve the current value of height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Modify the value of height

        Args:
            value (int): integer value
        """

        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
