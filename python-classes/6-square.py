#!/usr/bin/python3
"""Module that defines a Square class with size and position"""


class Square:
    """Class that defines a square by size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square

        Args:
            size (int): The size of the square
            position (tuple): The position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__size_position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation

        Args:
            value (tuple): tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size_position = value

    def area(self):
        """Calculates the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # considering its position"""
        if self.__size == 0:
            print("")
            return

        # Print new lines for vertical position (Y coordinate)
        for i in range(self.__size_position[1]):
            print("")

        # Print the square with horizontal spaces (X coordinate)
        for i in range(self.__size):
            print(" " * self.__size_position[0] + "#" * self.__size)
