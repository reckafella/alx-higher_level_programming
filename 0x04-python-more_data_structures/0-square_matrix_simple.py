#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_copy = []

    for row in range(len(matrix)):
        a = []

        for column in range(len(matrix[row])):
            a.append(matrix[row][column] ** 2)
        matrix_copy.append(a)

    return (matrix_copy)
