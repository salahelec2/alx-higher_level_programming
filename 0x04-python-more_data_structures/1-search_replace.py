#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for idx, value in enumerate(new_list):
        if value == search:
            new_list[idx] = replace
    return new_list
