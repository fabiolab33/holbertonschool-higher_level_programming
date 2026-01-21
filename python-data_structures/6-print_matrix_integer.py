#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers, one row per line,
    integers separated by spaces, using str.format().
    """
    for row in matrix:
        for i, val in enumerate(row):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(val), end="")
        print()
