#!/usr/bin/python3
"""return True if the object is exactly an instance of the specified class otherwise False"""


def is_same_class(obj, a_class):
    """Exact same object"""
    if type(obj) is a_class:
        return True
    else:
        return False
