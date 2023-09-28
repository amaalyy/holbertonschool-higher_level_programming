#!/usr/bin/python3
for x in range(0, 10):
    for o in range(x + 1, 10):
        if (x == 8 and o == 9):
            print("{}{}".format(x, o))
        else:
            print("{}{}".format(x, o), end=", ")
