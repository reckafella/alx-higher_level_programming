#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            if (b < (len(matrix[a]))):
                print("{}".format(matrix[a][b]), end=' ')
            else:
                print("{}".format(matrix[a][b]))
        print()
