#!/usr/bin/python3
"""
A file that define BaseGeometry class
"""


class BaseGeometry:
    """BaseGeometry class"""

    @classmethod
    def area(self):
        """method fo area calculation"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validating the value type"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
