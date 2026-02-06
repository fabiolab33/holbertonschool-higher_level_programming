#!/usr/bin/env python3
"""
Module that defines the CountedIterator class.
"""


class CountedIterator:
    """
    An iterator that keeps track of how many items have been iterated.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator and the counter.
        """
        self.__iterator = iter(iterable)
        self.__counter = 0

    def get_count(self):
        """
        Returns the current number of items iterated.
        """
        return self.__counter

    def __next__(self):
        """
        Fetches the next item and increments the counter.
        """
        try:
            # Intentamos obtener el siguiente elemento
            item = next(self.__iterator)
            # Si tiene éxito, incrementamos el contador
            self.__counter += 1
            return item
        except StopIteration:
            # Si no hay más elementos, lanzamos StopIteration
            raise StopIteration

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self
