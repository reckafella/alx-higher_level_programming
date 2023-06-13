#!/usr/bin/python3

""" Module contains a function to read and print contents of a text file """


def read_file(filename=""):
    """
    Read and print contents of a text file

    Args:
        filename (str): name of file to open
    """

    with open(filename, 'rt', encoding='UTF8') as f:
        print("{}".format(f.read()))
        f.close()
