#!/usr/bin/python3
"""
Module for text indentation.

This module provides a function to print text with proper indentation
after specific punctuation marks.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: A string to be printed with indentation

    Raises:
        TypeError: If text is not a string

    Examples:
        >>> text_indentation("Hello. World")
        Hello.
        <BLANKLINE>
        World

        >>> text_indentation("What? Really")
        What?
        <BLANKLINE>
        Really

        >>> text_indentation("Note: Important")
        Note:
        <BLANKLINE>
        Important
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Process the text
    i = 0
    while i < len(text):
        # Print current character
        print(text[i], end="")

        # Check if current character is one of the special punctuation
        if text[i] in '.?:':
            # Print 2 new lines
            print("\n")

            # Skip any spaces after the punctuation
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        i += 1