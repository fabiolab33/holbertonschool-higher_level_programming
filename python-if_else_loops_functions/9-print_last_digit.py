#!/usr/bin/python3
# Function that prints and returns
# the last digit of a number

def print_last_digit(number):
    """
    Prints and returns the last digit of a number.
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
