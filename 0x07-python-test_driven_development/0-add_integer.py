#!/usr/bin/python3
"""Files that define a function that adds two integers."""


def add_integer(a, b=98):
    """a function that adds 2 integers"""
    if type(a) not in (float, int) or a is None:
        raise TypeError("a must be an integer")
    if type(b) not in (float, int) or b is None:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
