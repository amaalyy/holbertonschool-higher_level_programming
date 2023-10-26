#!/usr/bin/python3
"""class base"""


class Base:
    """private class"""
    __nb_objects = 0
    """class constructor"""

    def __init__(self, id=None):
        if id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
