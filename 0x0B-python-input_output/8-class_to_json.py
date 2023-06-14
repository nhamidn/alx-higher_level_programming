#!/usr/bin/python3
"""File that define a class_to_json function"""


def class_to_json(obj):
    """Function that return a dict of the variables in object"""
    return vars(obj)
