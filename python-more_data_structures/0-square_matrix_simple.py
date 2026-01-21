#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square of all integers in a 2D matrix.

    Args:
        matrix (list of lists of int): Input 2D matrix

    Returns:
        list of lists of int: New 2D matrix with squared values
    """
    return [[value ** 2 for value in row] for row in matrix]
