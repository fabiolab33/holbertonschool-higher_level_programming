#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Delete the item at a specific position in a list.

    If idx is negative or out of range, return the same list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Shift elements to the left, effectively deleting the element
    for i in range(idx, len(my_list) - 1):
        my_list[i] = my_list[i + 1]
    # Remove the last duplicate element
    my_list[:] = my_list[:-1]

    return my_list
