#!/usr/bin/python3
"""Safe prints an integer."""

def safe_print_integer(value):
    """Prints an integer and returns True if successful, otherwise False."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
    