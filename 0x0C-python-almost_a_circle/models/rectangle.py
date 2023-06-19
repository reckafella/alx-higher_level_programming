#!/usr/bin/python3

""" Module containing Rectangle class that inherits from Base """
from .base import Base


class Rectangle(Base):
    """
    Rectangle: Inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Return value of width variable """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set value of width """
        self.__width = value

    @property
    def height(self):
        """ Return value of height variable """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set value of height """
        self.__height = value

    @property
    def x(self):
        """ Return value of x variable """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set value of x """
        self.__x = value

    @property
    def y(self):
        """ Return value of y variable """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set value of y """
        self.__y = value
