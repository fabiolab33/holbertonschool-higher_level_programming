#!/usr/bin/env python3
"""
Módulo para demostrar Clases Abstractas y Duck Typing.
"""
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
    """Representación de un círculo que maneja radios negativos."""

    def __init__(self, radius):
        # Usamos abs() para que el test de radio negativo pase
        self.radius = abs(radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Representación de un rectángulo que maneja dimensiones negativas."""

    def __init__(self, width, height):
        # Usamos abs() en ambos para asegurar resultados positivos
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Función que utiliza Duck Typing para imprimir información de la figura.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
