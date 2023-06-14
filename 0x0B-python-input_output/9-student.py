#!/usr/bin/python3
"""File that define a Student class"""


class Student:
    """a Student class"""

    def __init__(self, first_name, last_name, age):
        """Init method of Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of the obj"""
        return self.__dict__
