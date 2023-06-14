#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""
File that define a Square class
"""


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size):
        """Init method of the Square class"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Method that calulate the area of a Square"""

        return self.__size ** 2
