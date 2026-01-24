#!/usr/bin/python3
"""
This module provides a function to add two integers.

The function ensures that the provided arguments are integers or floats
and raises appropriate exceptions otherwise.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    a and b must be integers or floats, otherwise a TypeError is raised.
    Floats are casted to integers before the addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
