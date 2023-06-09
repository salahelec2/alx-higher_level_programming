#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    number = 0
    if my_list is None:
        my_list = []
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            number += 1
        except IndexError:
            continue
    print()
    return number
