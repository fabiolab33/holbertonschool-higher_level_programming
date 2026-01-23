#!/usr/bin/python3
"""Divides two integers and prints the result."""


def safe_print_division(a, b):
    """Divides two integers, prints the result and returns it."""
    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result
