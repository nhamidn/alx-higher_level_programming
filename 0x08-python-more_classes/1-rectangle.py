#!/usr/bin/python3
"""This file defines a Rectangle class."""


class Rectangle:
    """A class that defines a Rectangle with width and height"""
    def __init__(self, width=0, height=0):
        """Init method of the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter of __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of __width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter of __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of __height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
