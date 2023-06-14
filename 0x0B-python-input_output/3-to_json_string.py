#!/usr/bin/python3
"""File that define to_json_string function"""


import json


def to_json_string(my_obj):
    """function that returns the JSON representation"""
    return json.dumps(my_obj)
