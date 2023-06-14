#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        del a_dictionary[key]
    return a_dictionary

def print_sorted_dictionary(a_dictionary):
    ordered_keys = sorted(a_dictionary.keys())

    for key in ordered_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
