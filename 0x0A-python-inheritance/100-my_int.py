#!/usr/bin/python3
"""File that define MyInt Class"""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, other):
        """Return True if self and other not equal, else false"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return True if self and other equal, else false"""
        return super().__eq__(other)
