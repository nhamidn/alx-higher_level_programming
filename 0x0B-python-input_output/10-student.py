#!/usr/bin/python3
"""File that define a Student class"""


class Student:
    """a Student class"""

    def __init__(self, first_name, last_name, age):
        """Init method of Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the obj"""
        if attrs is None:
            return self.__dict__
        dic = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dic[key] = value
        return dic
