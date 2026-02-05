#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method"""


class BaseGeometry:
    """A class representing base geometry with an unimplemented area method"""

    def area(self):
        """Raises an Exception indicating that the method is not implemented
        
        Raises:
            Exception: always, because the area is not implemented here
        """
        raise Exception("area() is not implemented")
    