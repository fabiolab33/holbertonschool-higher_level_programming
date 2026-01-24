#!/usr/bin/python3
"""
Module for printing squares.

This module provides a function to print a square using the # character.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: An integer representing the size length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0

    Examples:
        >>> print_square(4)
        ####
        ####
        ####
        ####

        >>> print_square(1)
        #

        >>> print_square(0)
    """
    # Check if size is a float
    # (must check before int, since float < 0 needs TypeError)
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        print("#" * size)