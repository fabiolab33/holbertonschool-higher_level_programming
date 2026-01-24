#!/usr/bin/python3
"""
This module provides a function to divide all elements
of a matrix by a given number.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide
        div (int/float): The number to divide by

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        list of lists: New matrix with elements divided by div, rounded to 2 decimals
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = None
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)

    return new_matrix
