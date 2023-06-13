#!/usr/bin/python3

""" Class that inherits from "list" """


class MyList(list):
    """
    Class that inherits from list\
    and prints the list appended in ascending order

    Args:
        list (list): BaseClassName
    """

    def __init__(self):
        """ Initialize MyList by inheriting the properties of list """
        super().__init__(self)

    def print_sorted(self):
        """ Print the list in ascending order """
        print(sorted(self))
