#!/usr/bin/python3
"""
Module for matrix division.

This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats
        div: A number (integer or float) to divide by

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimals

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows of matrix have different sizes
        TypeError: If div is not a number
        ZeroDivisionError: If div is zero

    Examples:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

        >>> matrix_divided([[10, 20], [30, 40]], 2)
        [[5.0, 10.0], [15.0, 20.0]]
    """
    # Error message for invalid matrix
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if matrix is a list
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)

    # Check if matrix is a list of lists
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_msg)

    # Check if all elements are int or float
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(err_msg)

    # Check if all rows have the same size
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create new matrix with divided values
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix