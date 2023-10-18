#!/usr/bin/python3
"""return True if the object is exactly an instance of 
the specified class otherwise False"""


def is_same_class(obj, a_class):
    """ this is the function and it returns True or False"""
    if type(obj) is a_class:
        return True
    else:
        return False
