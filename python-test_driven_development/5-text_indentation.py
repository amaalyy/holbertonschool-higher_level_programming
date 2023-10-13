#!/usr/bin/python3
def text_indentation(text):
    if type(test) != str:
        raise TypeError("text must be a string")
    chars = [".", "?", ":"]
    for char in chars:
        text = text.replace(char, char + "\n\n")
    print(text.strip(), end= "")
