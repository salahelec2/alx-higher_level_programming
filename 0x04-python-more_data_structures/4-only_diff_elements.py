#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for elm in set_1:
        if elm not in set_2:
            new_set.add(elm)
    for elm in set_2:
        if elm not in set_1:
            new_set.add(elm)
    return new_set
