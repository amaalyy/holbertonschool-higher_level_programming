#!/usr/bin/python3
"""class of square"""


class Square:
    """__init__ method"""

    def __init__(self, size=0):
        self.__size = size
    """property"""
    @property
    def size(self):
        return self.__size
    """setter method"""
    @size.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """area method"""

    def area(self):
        return self.__size**2
