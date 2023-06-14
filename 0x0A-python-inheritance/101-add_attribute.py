#!/usr/bin/python3
"""File that define add_attribute function"""


def add_attribute(obj, attr, value):
    """function that adds a new attribute to an object"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
