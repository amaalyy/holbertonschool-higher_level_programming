#!/usr/bin/python3
def text_indentation(text):
    for i in range(len(text)):
        if text[i] == '.' or text[i] == "?" or text[i] == ":":
            print(text[i])
            print()
            print()
        else:
            print(text[i], end="")
