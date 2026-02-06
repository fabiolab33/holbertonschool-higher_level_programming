#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Clase abstracta que define la interfaz para figuras geométricas."""

    @abstractmethod
    def area(self):
        """Calcula el área de la figura."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcula el perímetro de la figura."""
        pass

class Circle(Shape):
    """Representación de un círculo."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Representación de un rectángulo."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Función que utiliza Duck Typing. 
    No verifica el tipo, solo confía en que el objeto tiene los métodos necesarios.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
