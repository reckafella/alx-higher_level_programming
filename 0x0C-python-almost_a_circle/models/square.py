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

    def update(self, *args, **kwargs):
        """
        assigns attributes:

        *args is the list of arguments - no-keyworded arguments
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        **kwargs must be skipped if *args exists and is not empty
        """
        if (args is not None and len(args) > 0):
            for i in range(len(args)):
                if i == 0:
                    Rectangle.update(self, id=args[i])
                if i == 1:
                    Rectangle.update(self, width=args[i], height=args[i])
                if i == 2:
                    Rectangle.update(self, x=args[i])
                if i == 3:
                    Rectangle.update(self, y=args[i])
        else:
            if (kwargs is not None and len(kwargs) > 0):
                for key, value in kwargs.items():
                    if key == 'id':
                        Rectangle.update(self, id=value)
                    if key == 'size':
                        Rectangle.update(self, width=value, height=value)
                    if key == 'x':
                        Rectangle.update(self, x=value)
                    if key == 'y':
                        Rectangle.update(self, y=value)
