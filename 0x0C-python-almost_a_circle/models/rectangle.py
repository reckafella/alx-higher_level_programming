#!/usr/bin/python3

""" Module containing Rectangle class that inherits from Base """
from .base import Base


class Rectangle(Base):
    """
    Rectangle: Inherits from Base
    """

    hash_symbol = '#'
    space_symbol = ' '

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

        if (self.__y > 0):
            print('{}'.format('\n' * self.__y), end='')
        for i in range(self.__height):
            if (self.__x > 0):
                print('{}'.format(self.space_symbol * self.__x), end='')
            for j in range(self.__width):
                print("{}".format(self.hash_symbol), end='')
            print()

    def __str__(self):
        """ override the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return '[{}] ({}) {}/{} - {}/{}'.format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute:

        Args:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        if args is not None and len(args) >= 1:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
        else:
            if (kwargs is not None and len(kwargs) >= 1):
                for key, value in kwargs.items():
                    if (key == 'width'):
                        self.__width = value
                    if (key == 'height'):
                        self.__height = value
                    if (key == 'x'):
                        self.__x = value
                    if (key == 'id'):
                        self.id = value
                    if (key == 'y'):
                        self.__y = value
