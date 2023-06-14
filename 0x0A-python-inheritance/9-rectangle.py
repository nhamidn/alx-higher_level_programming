#!/usr/bin/python3
"""
File that define a Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Init method of the class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method that override the method of the parent class"""

        return self.__width * self.__height

    def __str__(self):
        """Method that return the string representation"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
