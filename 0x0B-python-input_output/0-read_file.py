#!/usr/bin/python3
"""File that define a read_file function"""


def read_file(filename=""):
    """Function that reads a text file and prints it"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
