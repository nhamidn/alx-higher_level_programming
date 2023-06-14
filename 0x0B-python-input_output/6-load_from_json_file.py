#!/usr/bin/python3
"""File that define load_from_json_file function"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file"""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
