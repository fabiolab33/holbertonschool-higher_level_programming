#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value in a dictionary.

    Args:
        a_dictionary (dict): Dictionary to update
        key (str): Key to update or add
        value: Value to assign to the key

    Returns:
        dict: The updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
