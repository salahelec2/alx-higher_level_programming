#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_ls = my_list[::-1]
    for element in reversed_ls:
        print("{:d}".format(element))
