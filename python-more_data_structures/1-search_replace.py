#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    Args:
        my_list (list): The original list
        search: Element to be replaced
        replace: New element

    Returns:
        list: A new list with replaced elements
    """
    return [replace if item == search else item for item in my_list]
