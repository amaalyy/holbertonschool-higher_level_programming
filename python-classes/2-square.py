#!/usr/bin/python3
"""class square"""
class Square:
    """"class square"""
    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size must me >=0")
        self.__size = size
