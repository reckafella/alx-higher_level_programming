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
    i, j = 0, 0
    single_line = ""
    new_str = ""

    if text is None:
        raise TypeError("text_indentation() missing 1 required\
                        positional argument: 'text'")
    elif not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if (text[i] == '.' or text[i] == '?' or text[i] == ':'):
            single_line += "\n\n"
            new_str += single_line.strip()
        else:
            single_line += text[i]

    for j in range(len(new_str)):
        print(new_str[j], end="")
