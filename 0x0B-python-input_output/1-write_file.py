#!/usr/bin/python3

""" Module contains a function to write a string into a text file """


def write_file(filename="", text=""):
    """
    Write characters of a string to of a text file

    Args:
        filename (str): name of file to open
        text (str): string written to text file
    """
    nchars = 0

    with open(filename, 'w', encoding='UTF8') as f:
        for char in text:
            f.write(char)
            nchars += 1
    return nchars
