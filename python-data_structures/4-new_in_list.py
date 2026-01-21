#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position without
    modifying the original list.

    If idx is negative or out of range, return a copy of the list.
    """
    new_list = my_list[:]  # Line copies the original list
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
