#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        j = 0
        for i in my_list:
            if j < x and type(i) == int:
                print("{:d}".format(i), end="")
                j += 1
    except BaseException:
        raise IndentationError("list index out of range")
    print(end="\n")
    return j
