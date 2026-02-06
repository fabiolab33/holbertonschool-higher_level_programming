#!/usr/bin/env python3
"""
Módulo que define la clase abstracta Animal y sus subclases Dog y Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Clase base abstracta que define la estructura para todos los animales.
    """

    @abstractmethod
    def sound(self):
        """
        Método abstracto que debe ser implementado por las subclases.
        """
        pass


class Dog(Animal):
    """
    Subclase de Animal que implementa el sonido de un perro.
    """

    def sound(self):
        """
        Retorna el sonido característico de un perro.
        """
        return "Bark"


class Cat(Animal):
    """
    Subclase de Animal que implementa el sonido de un gato.
    """

    def sound(self):
        """
        Retorna el sonido característico de un gato.
        """
        return "Meow"
