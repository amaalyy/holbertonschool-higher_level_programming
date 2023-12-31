#!/usr/bin/python3
"""Class of Square"""


class Square:

    """__init__ method"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """property"""
    @property
    def size(self):
        return (self.__size)

    """size_setter method"""
    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """property"""
    @property
    def position(self):
        return (self.__position)

    """setter method"""
    @position.setter
    def position(self, value):
        if (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """area method"""

    def area(self):
        return (self.__size**2)

    """print_square method"""

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                print(' ' * self.__position[0], end="")
                for j in range(self.__size):
                    print('#', end="")
                print(end='\n')
