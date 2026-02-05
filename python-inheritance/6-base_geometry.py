#!/usr/bin/python3
"""Module that defines a BaseGeometry class"""


class BaseGeometry:
    """Class representing base geometry"""

    def area(self):
        """Method that raises an Exception

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
