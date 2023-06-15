#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = []
    new_d = dict(a_dictionary)
    for key, val in new_d.items():
        if val == value:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del new_d[key]
    return new_d
