#!/usr/bin/python3

"""
A module containing a function that divides all elements of a matrix.

Prototype: def matrix_divided(matrix, div):
 * matrix must be a list of lists of integers or floats, otherwise raise a
 TypeError exception with the message matrix must be a matrix (list of lists)
 of integers/floats
* Each row of the matrix must be of the same size, otherwise raise a TypeError
exception with the message Each row of the matrix must have the same size
* div must be a number (integer or float), otherwise raise a TypeError
exception with the message div must be a number
* div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with
the message division by zero
* All elements of the matrix should be divided by div, rounded to 2 decimal
places
* Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix.

    Args:
        matrix (list): list of lists of integers / floats
        div (int / float): integer value

    Returns:
        A new matrix if no error occurs.
    """

    if not isinstance(matrix, list)\
        or not all(isinstance(row, list) for row in matrix)\
        or not all((
            isinstance(
            value, (int, float)) for value in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Each row of the matrix must have the same size")

    elif not (isinstance(div, (float, int))):
        raise TypeError("div must be a number")

    elif (div == 0):
        raise ZeroDivisionError("division by zero")

    else:
        new = []

        for row in matrix:
            new_row = []
            for element in row:
                new_element = round(element / div, 2)
                new_row.append(new_element)
            new.append(new_row)

        return new
