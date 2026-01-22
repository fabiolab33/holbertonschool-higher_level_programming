#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the highest value in a dictionary.

    Args:
        a_dictionary (dict): Dictionary of scores

    Returns:
        str: Key with the highest score, or None if the dictionary is empty or None
    """
    if not a_dictionary:
        return None

    best_key = None
    best_value = None

    for key, value in a_dictionary.items():
        if best_value is None or value > best_value:
            best_value = value
            best_key = key
    return best_key