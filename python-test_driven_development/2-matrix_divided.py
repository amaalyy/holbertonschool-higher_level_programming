#!/usr/bin/python3
"""devide matrix"""


def matrix_divided(matrix, div):
    new_mat = []
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        new_mat1 = []
        c = len(matrix[0])
        if c != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(matrix[i], list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for j in range(len(matrix[i])):
            if not isinstance(
                    matrix[i][j],
                    int) and not isinstance(
                    matrix[i][j],
                    float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            else:
                new_mat1.append(round(matrix[i][j] / div, 2))
        new_mat.append(new_mat1)
    return new_mat
