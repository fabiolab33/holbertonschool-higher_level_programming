#!/usr/bin/python3
"""Divides elements by elements two lists."""


def list_division(my_list_1, my_list_2, list_lenght):
    """Divedes two lists element by element."""
    result = []

    for i in range(list_lenght):
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            result.append(division)

    return result