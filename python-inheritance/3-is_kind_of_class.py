#!/usr/bin/python3
"""Module that contains the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or inherited from, a_class

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if matches, otherwise False
    """
    return isinstance(obj, a_class)
