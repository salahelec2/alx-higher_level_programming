#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for elm in set_1:
        for elm2 in set_2:
            if elm == elm2:
                new_set.add(elm)
    return new_set
