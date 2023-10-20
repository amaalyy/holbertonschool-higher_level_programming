#!/usr/bin/python3
"""import the class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle
"""class Rectangle"""


class Square(Rectangle):
    """Square #1"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    """return Square description"""
    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
