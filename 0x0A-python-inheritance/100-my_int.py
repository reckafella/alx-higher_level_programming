#!/usr/bin/python3

""" This module contains a class MyInt that inherits from int """


class MyInt(int):
    """ Extends properties of int """

    def __eq__(self, number):
        """ Invert == """
        return super().__ne__(number)

    def __ne__(self, number):
        """ Invert != """
        return super().__eq__(number)
