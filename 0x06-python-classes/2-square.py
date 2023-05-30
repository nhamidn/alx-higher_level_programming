#!/usr/bin/python3
"""File that define a square class."""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """Init function of the class"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
