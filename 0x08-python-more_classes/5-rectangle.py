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

    def area(self):
        """
        Return the area of a rectangle given width and height
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """
        Return the perimeter of a rectangle given width and height

        Return 0 if either width or height is equal to 0
        """
        if (self.__height == 0 or self.__width == 0):
            return 0
        else:
            return ((2 * self.__height) + (2 * self.__width))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __str__(self):
        """
        Return the string representation of the rectangle using # symbol
        """
        one_line = ""
        if (self.__height == 0 or self.__width == 0):
            return one_line

        for i in range(self.__height):
            if (i < (self.__height - 1)):
                one_line += "#" * self.__width + "\n"
            else:
                one_line += "#" * self.__width
        return one_line

    def __del__(self):
        """
        Detects an instance where a Rectangle object is deleted
        """
        print("{}".format("Bye rectangle..."))
