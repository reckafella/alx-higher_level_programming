#!/usr/bin/python3

BaseGeometry = __import__("7-base_geometry").BaseGeometry

""" This module creates a  class Rectangle that inherits from BaseGeometry\
(7-base_geometry.py). """


class Rectangle(BaseGeometry):
    """ This class extends BaseGeometry """

    def __init__(self, width, height):
        """ Initialize the current object """
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
