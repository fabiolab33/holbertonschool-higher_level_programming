#!/usr/bin/python3
"""
Module for printing names.

This module provides a function to print a formatted name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'.

    Args:
        first_name: A string representing the first name
        last_name: A string representing the last name (optional, default "")

    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith

        >>> say_my_name("Walter", "White")
        My name is Walter White

        >>> say_my_name("Bob")
        My name is Bob 
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted name
    print("My name is {} {}".format(first_name, last_name))