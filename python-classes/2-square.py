#!/usr/bin/python3
"""class square"""


class Square:
    """"class square"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must me >=0")
        else:
            self.__size = size
        