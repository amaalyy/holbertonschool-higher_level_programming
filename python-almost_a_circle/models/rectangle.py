#!/usr/bin/python3

"""import class Base"""
from python-almost_a_circle.a import height
from models.base import Base

"""Class Rectangle"""


class Rectangle(Base):

    """__init__ method"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    # width property
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if (type(width) != int):
            raise TypeError(f"{width} of the attribute> must be an integer")
        elif (width <= 0):
            raise ValueError(f"{width} of the attribute> must be > 0")
        else:
            self.__width = width

    # height property
def height(self):
    @height.setter
    def height(self, height):
        if (type(height) == int):
            raise TypeError(f"{height} of the attribute> must be an integer")
        elif (height <= 0):
            raise ValueError(f"{height} of the attribute> must be > 0")
        else:
            self.__height = height

    # x property
def x(self):
    @x.setter
    def x(self, x):
        if (type(x) == int):
            raise TypeError(f"{x} of the attribute> must be an integer")
        elif (x <= 0):
            raise ValueError(f"{x} must be >= 0")
        else:
            self.__x = x

    # y property
def y(self):
    @y.setter
    def y(self, y):
        if (type(y) == int):
            raise TypeError(f"{y} of the attribute> must be an integer")
        elif (y <= 0):
            raise ValueError(f"{y} must be >= 0")
        else:
            self.__y = y
