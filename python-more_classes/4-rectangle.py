#!/usr/bin/python3
"""Module that defines a Rectangle class with __repr__"""


class Rectangle:
    """Class that defines a rectangle by its width and height"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional size"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with integer and positive validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with integer and positive validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter (0 if any side is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns a string representation with # for visual printing"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_rows = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rect_rows)

    def __repr__(self):
        """Returns a string representation to recreate the object with eval()"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
