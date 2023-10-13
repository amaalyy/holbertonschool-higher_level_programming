#!/usr/bin/python3
"""class of Rectangle"""


class Rectangle:
    """__init__ method"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
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
        x = ""
        if self.width == 0 or self.height == 0:
            return (x)
        else:
            x = ""
            for i in range(self.height):
                for j in range(self.width):
                    x += (str(self.print_symbol)*self.width)
                if self.height - 1 != i:
                    x += '\n'
            return x
    """string representation of the rectangle"""

    def __repr__(self):
        return f"Rectangle({self.__width},{self.__height})"
    """__del__ method an instance of Rectangle is deleted"""

    def __del__(self):
        Rectangle.number_of_instances -= 1   
        print("Bye rectangle...")
