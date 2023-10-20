#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """Improve Geometry"""

    def area(self):
        raise Exception("area() is not implemented")
    """Integer validator"""

    def integer_validator(self, name, value):
        self.name = name
        if (not isinstance(value, int)):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
        else:
            self.value = value
