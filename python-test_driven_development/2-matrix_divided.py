#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.

The matrix must be a list of lists containing integers or floats,
and all rows must have the same size.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): Matrix of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: New matrix with divided values rounded to 2 decimals.
    """
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = None

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
