#!/usr/bin/python3

"""import the class BaseGeometry"""
Rectangle = __import__('7-base_geometry').BaseGeometry


"""class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):

    """Rectangle """

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.height = self.integer_validator("height", height)
