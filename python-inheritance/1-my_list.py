#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """My list"""

    def print_sorted(self):
        print(sorted(self))
