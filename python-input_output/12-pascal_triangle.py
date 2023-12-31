#!/usr/bin/python3
"""function def pascal_triangle(n): that returns a
list of lists of integers representing the triangle of n"""


def pascal_triangle(n):
    """Pascal's Triangle """
    res = []
    if (n <= 0):
        return res
    for i in range(n):
        if i == 0:
            res.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(res[i - 1][j - 1] + res[i - 1][j])
            row.append(1)
            res.append(row)
    return res
