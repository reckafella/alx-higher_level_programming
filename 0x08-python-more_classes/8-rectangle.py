#!/usr/bin/python3

""" This module implements a class Rectangle """


class Rectangle:
    """ This class is a representation of a rectangle.

    Attributes:
        number_of_instances (int): number of instances of the class object
    """
    print_symbol = "#"
    number_of_instances = 0

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

        Rectangle.number_of_instances += 1

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
        text = ""
        if (self.__height == 0 or self.__width == 0):
            return text

        for i in range(self.__height):
            if (i < (self.__height - 1)):
                text += "{}\n".format(str(self.print_symbol) * self.__width)
            else:
                text += "{}".format(str(self.print_symbol) * self.__width)
        return text

    def __del__(self):
        """
        Detects an instance where a Rectangle object is deleted
        """
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            area_rect_1 = rect_1.area()
            area_rect_2 = rect_2.area()

            if (area_rect_1 > area_rect_2 or area_rect_1 == area_rect_2):
                return rect_1
            else:
                return rect_2
