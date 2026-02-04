#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list"""


class MyList(list):
    """Class that inherits from list with a sorted print method"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
