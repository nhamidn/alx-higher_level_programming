#!/usr/bin/python3

def matrix_divided(matrix, div):
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(msg)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(msg)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
