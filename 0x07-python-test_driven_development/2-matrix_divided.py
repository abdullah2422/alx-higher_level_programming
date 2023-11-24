#!/usr/bin/python3
"""
Module matrix_divided
"""


def matrix_divided(matrix, div):
    """Returns a new matrix (list of lists)
    """
    if type(matrix) is not list or any(type(row) is not list for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int , float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
