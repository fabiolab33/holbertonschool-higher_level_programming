#!/usr/bin/env python3
"""
Module that explores multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Standard swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Standard fish habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Standard flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Standard bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A flying fish that inherits from both Fish and Bird.
    Demonstrates multiple inheritance and MRO.
    """

    def fly(self):
        """Overrides Bird's fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides Fish's swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides both parents' habitat method."""
        print("The flying fish lives both in water and the sky!")
