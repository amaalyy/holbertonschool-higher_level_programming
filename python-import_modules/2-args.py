#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv) - 1
    if x == 0:
        print("0 argments.")
    elif x == 1:
        print("1 arguments")
    else:
        print("{} arguments:".format(x))
    for x in range(x):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
