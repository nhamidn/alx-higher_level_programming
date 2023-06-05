#!/usr/bin/python3
"""This file defines a Rectangle class."""


class Rectangle:
    """A class that defines a Rectangle with width and height"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Init method of the class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Return the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Return the rectangle as string with the character #"""
        str_rec = ""
        if self.__height == 0 or self.width == 0:
            return str_rec
        for i in range(self.__height):
            str_rec += ("#" * self.__width)
            if i is not self.__height - 1:
                str_rec += "\n"
        return str_rec

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print message when the instance if deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
