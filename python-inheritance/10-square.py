#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square using Rectangle logic"""

    def __init__(self, size):
        """Initialize the square with a private size

        Args:
            size (int): The size of the square's sides
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square"""
        return self.__size ** 2
