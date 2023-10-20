#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """Improve Geometry"""

    def area(self):
        raise Exception("area() is not implemented")
    """Integer validator"""

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

