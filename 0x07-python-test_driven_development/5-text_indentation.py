#!/usr/bin/python3

"""
Module contains a function that prints a text with 2 new lines after each of\
these characters: ., ? and :

Prototype: def text_indentation(text):
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of
    these characters: ., ? and :
    Args:
        text: string
    """

    if text is None:
        raise TypeError("text_indentation() missing 1\
                        required positional argument: 'text'")
    elif not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for char in text:
            if (char == '.' or char == '?' or char == ':'):
                print()
                print()
            else:
                print("{}".format(char), end="")
