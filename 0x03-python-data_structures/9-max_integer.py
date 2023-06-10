#!/usr/bin/python3
def max_integer(my_list):
    old_val = 0
    for i in my_list:
        if i > old_val:
            old_val = i
    return old_val
