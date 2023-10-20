#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """Improve Geometry"""

    def area(self):
        raise Exception("area() is not implemented")
    """Integer validator"""

    def integer_validator(self, name, value):
        self.name = name
        if type(value) != int:
            raise TypeError(f"{self.name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
        else:
            self.value = value
