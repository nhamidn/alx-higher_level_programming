#!/usr/bin/python3
"""File that define a append_write function"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of afile"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
