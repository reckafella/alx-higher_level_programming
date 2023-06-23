#!/usr/bin/python3

""" Module contains Square class that extends Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class extends Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize Square by using logic of __init__ from Rectangle class

        Args:
            size (int)
            x (int)
            y (int)
            id (int)
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """ Override __str__ method from Rectangle class """
        return '[{}] ({}) {}/{} - {}'.format(self.__class__.__name__,
                                             self.id, super().x,
                                             super().y, super().height)

    @property
    def size(self):
        """ Return the value of size """
        return super().width

    @size.setter
    def size(self, size):
        """
        Sets the value of width and height to size

        Args:
            size (int): length of one side of square
        """
        Rectangle(width=size, height=size)
        Rectangle.width = size
        Rectangle.height = size
