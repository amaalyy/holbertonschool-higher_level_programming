#!/usr/bin/python3
def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(1, size * size + 1):
        if i % size == 0:
            print('#')
        else:
            print("#", end="")
