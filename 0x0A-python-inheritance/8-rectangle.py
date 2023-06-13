#!/usr/bin/python3

BaseGeometry = __import__("7-base_geometry").BaseGeometry

""" This module creates a  class Rectangle that inherits from BaseGeometry\
(7-base_geometry.py). """


class Rectangle(BaseGeometry):
    """ This class extends BaseGeometry """

    def __init__(self, width, height):
        super().__init__()
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)


r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
