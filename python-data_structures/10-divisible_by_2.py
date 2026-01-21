#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Return a new list of booleans indicating if integers
    in the original list are divisible by 2.
    """
    result = []
    for num in my_list:
        result.append(num % 2 == 0)
    return result
