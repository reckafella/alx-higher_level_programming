#!/usr/bin/python3

""" Module contains a function to appends a string at end of a text file """


def append_write(filename="", text=""):
    """
    Append text characters to a text file

    Args:
        filename (str): name of file to open
        text (str): string written to text file
    """
    nchars = 0

    with open(filename, 'a', encoding='UTF8') as f:
        for char in text:
            f.write(char)
            nchars += 1
    return nchars
