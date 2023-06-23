#!/usr/bin/python3

""" Module contains Square class that extends Rectangle """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Class extends Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize Square by using logic of __init__ from Rectangle class
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)
