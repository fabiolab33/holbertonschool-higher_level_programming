#!/usr/bin/env python3
"""
Módulo que utiliza Mixins para dar habilidades a la clase Dragon.
"""


class SwimMixin:
    """Mixin que añade la habilidad de nadar."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin que añade la habilidad de volar."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Clase Dragon que hereda de dos Mixins.
    Demuestra cómo componer comportamientos sin una jerarquía rígida.
    """
    def roar(self):
        print("The dragon roars!")
