#!/usr/bin/python3
"""File that define save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file"""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
