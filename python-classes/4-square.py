#!/usr/bin/python3
"""Module that defines a Square class with properties"""


class Square:
    """Class that defines a square with getter and setter"""

    def __init__(self, size=0):
        """Initialize the square

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation

        Args:
            value (int): The new size of the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the current square area

        Returns:
            The square of the size
        """
        return self.__size ** 2
