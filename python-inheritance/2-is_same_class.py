#!/usr/bin/python3
"""return True if the object is exactly an instance of the specified class otherwise False"""


def is_same_class(obj, a_class):
    """Exact same object"""
    if (not isinstance(obj, a_class)):
        return False
    else:
        return True
