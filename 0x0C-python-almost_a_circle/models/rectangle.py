#!/usr/bin/python3

""" Module containing Rectangle class that inherits from Base """
from .base import Base


class Rectangle(Base):
    """
    Rectangle: Inherits from Base
    """

    print_symbol = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Method validates values passed as arguments """
        super().__init__(id)

        if (type(width) != int):
            raise TypeError('width must be an integer')
        elif (width <= 0):
            raise ValueError('width must be > 0')
        else:
            self.__width = width

        if (type(height) != int):
            raise TypeError('height must be an integer')
        elif (height <= 0):
            raise ValueError('height must be > 0')
        else:
            self.__height = height

        if (type(x) != int):
            raise TypeError('x must be an integer')
        elif (x < 0):
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

        if (type(y) != int):
            raise TypeError('y must be an integer')
        elif (y < 0):
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    @property
    def width(self):
        """ Return value of width variable """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set value of width """
        if (type(value) != int):
            raise TypeError('width must be an integer')
        elif (value <= 0):
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ Return value of height variable """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set value of height """
        if (type(value) != int):
            raise TypeError('height must be an integer')
        elif (value <= 0):
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ Return value of x variable """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set value of x """
        if (type(value) != int):
            raise TypeError('x must be an integer')
        elif (value < 0):
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ Return value of y variable """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set value of y """
        if (type(value) != int):
            raise TypeError('y must be an integer')
        elif (value < 0):
            raise ValueError('y must be >= 0')
        else:
            self.__x = value

    def area(self):
        """ Return area of the rectangle given width and height """
        return (self.__height * self.__width)

    def display(self):
        """ print in stdout the Rectangle instance with the character # """

        for i in range(self.__height):
            for j in range(self.__width):
                print("{}".format(self.print_symbol), end='')
            print()

    def __str__(self):
        """ override the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return '[{}] ({}) {}/{} - {}/{}'.format(
            self.__class__.__name__,self.id, self.__x, self.__y,
            self.__width, self.__height)
