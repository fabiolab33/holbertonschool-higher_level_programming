#!/usr/bin/env python3
"""
Module for Shapes, Interfaces, and Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculates the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a circle.
    """

    def __init__(self, radius):
        """
        Initializes a circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle, handling negative radius.
        """
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """
        Returns the perimeter of the circle, handling negative radius.
        """
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Concrete class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """
    Prints the area and perimeter of a shape using duck typing.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
