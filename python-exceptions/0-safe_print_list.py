#!/usr/bin/python3
"""Safe list printing with exception handling."""


def safe_print_list(my_list=[], x=0):
    """Print up to x elements of my_list and return the number printed."""
    count = 0
    while count < x:
        try:
            print(my_list[count], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
