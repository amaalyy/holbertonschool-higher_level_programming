#!/usr/bin/python3
"""check for ? . : and prints a text with 2 new lines"""


def text_indentation(text):
    """checking"""
    c = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == "?" or text[i] == "." or text[i] == ":":
            print(text[i])
            print()
            a = 1
        else:
            if c == 1 and text[i] == " ":
                c = 1
            else:
                c = 0
                print(text[i], end="")
