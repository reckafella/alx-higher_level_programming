#!/usr/bin/python3

"""
This module define a class Square which is used to handle the
the calculation of area of a square.
"""


class Square:
    """
    A class that defines a square.

    Args:
        size (int): size of a single side of a square

    Attributes:
        size (int): size of a single side of a square
        position (tuple): tuple of size 2
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method

        Args:
            size (int): size of a single side of a square
            position (tuple): tuple with two integer elements

        Attributes:
            size (int): size of a single side of a square
            position (tuple): tuple with two integer elements
        """

        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if ((type(position) == tuple) and (len(position) == 2)):
            self.__position = tuple(position)
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """
        This method returns the current value of 'size'
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Method validates the new value of size before updating size

        Attributes:
            value (int): integer passed to the class object
        """

        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        A method that returns the current square area
        """
        return (self.__size ** 2)

    @property
    def position(self):
        """
        Position retrieves the value of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This method is used to update the value of position

        Attributes:
            value (tuple): tuple with two elements
        """

        if ((type(value) == tuple) and (len(value) == 2)):
            self.__position = tuple(value)
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        Print the square as a series of # symbols.
        """

        if (self.__size > 0):
            for i in range(self.__size):
                if (self.__position[0] > 0):
                    print("{}".format(" " * self.__position[0]), end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
