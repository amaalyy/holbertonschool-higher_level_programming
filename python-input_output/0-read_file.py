#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Read file"""
    with open(filename, 'r', encoding="UTF8") as f:
        for c in f:
            print (c)
