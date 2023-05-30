#!/usr/bin/python3
"""File that define a square class."""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """Init method of the class"""
        self.size = size

    def area(self):
        """Function that calculate the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Getter of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of __size"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
