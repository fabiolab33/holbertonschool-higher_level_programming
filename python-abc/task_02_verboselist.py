#!/usr/bin/env python3
"""
Module that defines the VerboseList class.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications when modified.
    """

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list and prints a notification with the count."""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Prints notification before removing an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints notification before popping an item."""
        # Obtenemos el item antes de eliminarlo para poder imprimirlo
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
