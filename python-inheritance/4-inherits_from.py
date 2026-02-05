#!/usr/bin/python3
"""Module that contains the function inherits_from"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited from a_class

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if it inherits and is not the same class, otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
