#!/usr/bin/python3
"""class of Rectangle"""


class Rectangle:
    """__init__ method"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """retrive the width"""
    @property
    def width(self):
        return self.__width
    """set the width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    """retrive the height"""
    @property
    def height(self):
        return self.__height
    """set the height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    """calculate the retangle area"""

    def area(self):
        return self.__width * self.height
    """calculate the retangle perimeter"""

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            x = ""
            for i in range(self.height):
                for j in range(self.width):
                    x += "#"
                if self.height - 1 != i:
                    x += '\n'
            return x
    """string representation of the rectangle"""
    def __repr__(self):
        return (f"Rectangle({self.width},{self.__height})")
