#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for idx, value in enumerate(my_list):
        if value == search:
            my_list[idx] = replace
    return my_list
