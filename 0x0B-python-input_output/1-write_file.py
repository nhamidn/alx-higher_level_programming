#!/usr/bin/python3
"""File that define a write_file function"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
