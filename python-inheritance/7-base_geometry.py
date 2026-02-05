#!/usr/bin/python3
"""Module that defines a BaseGeometry class with integer validation"""


class BaseGeometry:
    """A class that provides basic geometric operations and validation"""

    def area(self):
        """Method that defines the area of a shape but is not implemented yet

        Raises:
            Exception: always, because this is a base class method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a given value is a strictly positive integer

        Args:
            name (str): The name associated with the value to validate
            value (int): The integer value to be checked

        Raises:
            TypeError: if the value is not a standard integer
            ValueError: if the value is equal to or less than zero
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
