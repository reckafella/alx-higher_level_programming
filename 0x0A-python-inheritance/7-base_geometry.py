#!/usr/bin/python3

""" Module defines a class BaseGeometry with instance method: area """


class BaseGeometry:
    """ Class BaseGeometry that adds "area" instance method """

    def area(self):
        """
        The method is not implemented

        Raises:
            Exception: since area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates the value of variable 'value'

        Args:
            name (str): name
            value (int): integer value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is not greater than 0
        """
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value
