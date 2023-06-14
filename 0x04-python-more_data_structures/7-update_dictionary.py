#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dictionary = dict()
    for elment in a_dictionary:
        new_dictionary.update({elment : a_dictionary[elment]})
    new_dictionary.update({key : value})
    return new_dictionary
