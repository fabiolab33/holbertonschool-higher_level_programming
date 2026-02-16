#!/usr/bin/python3
"""Module that demonstrates pickling of a custom class."""

import pickle


class CustomObject:
    """Custom class that supports serialization using pickle."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object to a file using pickle.

        Returns:
            True if successful, None otherwise.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
            return True
        except (FileNotFoundError, pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a pickle file.

        Returns:
            An instance of CustomObject if successful, None otherwise.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            return obj
        except (FileNotFoundError, pickle.PickleError,
                EOFError, OSError):
            return None
