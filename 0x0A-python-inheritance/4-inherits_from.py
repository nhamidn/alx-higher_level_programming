#!/usr/bin/python3
"""
File that define the inherits_from function
"""


def inherits_from(obj, a_class):
    """Function that check if the object is inheriting from"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
